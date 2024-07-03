import configparser
import json
import os
import time
from datetime import datetime
from typing import Optional, Union

import click
import pandas as pd
import requests
import yaml
from dotenv import load_dotenv

from morph.cli.flags import Flags
from morph.task.base import BaseTask
from morph.task.constant.project_config import ProjectConfig, ProjectPrefix
from morph.task.utils.code_execution import execute_user_code
from morph.task.utils.decorator import DecoratorParser
from morph.task.utils.logging import get_morph_logger
from morph.task.utils.morph import MorphYaml
from morph.task.utils.sql import SqlResultResponse, convert_sql_response
from morph.task.utils.sqlite import SqliteDBManager
from morph.task.utils.status import RunStatus
from morph.task.utils.timer import TimeoutException, run_with_timeout
from morph.task.utils.timezone import TimezoneManager


class RunTask(BaseTask):
    def __init__(self, args: Flags):
        super().__init__(args)

        # validate credentials
        config_path = ProjectConfig.MORPH_CRED_PATH
        if not os.path.exists(config_path):
            click.echo(f"Error: No credentials found in {config_path}.")
            raise FileNotFoundError(f"No credentials found in {config_path}.")

        # read credentials
        config = configparser.ConfigParser()
        config.read(config_path)
        if not config.sections():
            click.echo(f"Error: No credentials entries found in {config_path}.")
            raise FileNotFoundError(f"No credentials entries found in {config_path}.")

        # NOTE: vm内ではセクションが必ず1つなので、'default' セクションを指定している
        self.team_slug = config.get("default", "team_slug")
        self.app_url = config.get("default", "app_url")
        self.database_id = config.get("default", "database_id")
        self.api_key = config.get("default", "api_key")

        # create setup code
        self.setup_code = f"""\
from io import StringIO
import pandas as pd

import os
os.environ["MORPH_DATABASE_ID"] = "{self.database_id}"
os.environ["MORPH_BASE_URL"] = "{self.app_url}"
os.environ["MORPH_TEAM_SLUG"] = "{self.team_slug}"
os.environ["MORPH_API_KEY"] = "{self.api_key}"
"""

        # parse arguments
        self.filename = os.path.normpath(args.FILENAME)
        self.run_id = self.args.RUN_ID or f"{int(time.time() * 1000)}"
        self.is_dag = args.DAG or False
        self.is_dry_run = args.DRY_RUN or False

        try:
            start_dir = self.filename if os.path.isabs(self.filename) else "./"
            self.project_root = MorphYaml.find_abs_project_root_dir(start_dir)
        except FileNotFoundError as e:
            click.echo(click.style(str(e), fg="red"))
            raise e
        self.project_config_path = os.path.join(
            self.project_root, ProjectConfig.MORPH_YAML
        )

        # Initialize database
        self.db_path = os.path.join(self.project_root, "morph_project.sqlite3")
        self.db_manager = SqliteDBManager(self.project_root, self.db_path)
        self.db_manager.initialize_database()

        # Load morph.yaml
        self.morph_config = MorphYaml.init(self.project_root)

        # Find the file in morph.yaml if alias is provided
        if not os.path.splitext(os.path.basename(self.filename))[1]:
            resource = self.morph_config.resources.get(self.filename)
            self.filename = resource.get("path") if resource else None
            if not self.filename:
                click.echo(
                    click.style(
                        f"Error: Could not find the file {self.filename} in morph.yaml.",
                        fg="red",
                    )
                )
                raise FileNotFoundError(
                    f"Could not find the file {self.filename} in morph.yaml."
                )
        if not os.path.isabs(self.filename):
            self.filename = os.path.join(self.project_root, self.filename)
        if not os.path.exists(self.filename):
            click.echo(
                click.style(
                    f"Error: File {self.filename} not found.",
                    fg="red",
                )
            )
            raise FileNotFoundError(f"Error: File {self.filename} not found.")

        self.basename = os.path.splitext(os.path.basename(self.filename))[0]
        self.ext = os.path.splitext(os.path.basename(self.filename))[1]

        # Add file to morph.yaml if not present and get the alias
        self.cell_alias = self.morph_config.find_or_create_alias(
            self.filename, self.project_root, self.db_manager
        )
        self._save_morph_config()

        # Define output directory and filename
        self.output_dir = None
        self.output_filename = self.run_id
        resource = self.morph_config.resources.get(self.cell_alias)
        output_path = (
            os.path.normpath(resource.get("output_path"))
            if resource.get("output_path")
            else None
        )
        if output_path:
            output_path_full = os.path.normpath(
                os.path.join(self.project_root, output_path)
            )
            if os.path.isdir(output_path_full):
                self.output_dir = output_path_full
                self.output_filename = self.run_id
            else:
                self.output_dir = os.path.dirname(output_path_full)
                self.output_filename = os.path.splitext(os.path.basename(output_path))[
                    0
                ]
        if self.output_dir is None:
            self.output_dir = os.path.join(
                self.project_root,
                "src",
                ProjectConfig.OUTPUTS_DIR,
                f"{ProjectPrefix.OUTPUTS_PREFIX}{self.cell_alias}",
            )
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self.canvas = args.CANVAS
        if (
            self.canvas
            and self.cell_alias
            and not self.morph_config.canvases.get(self.canvas, {}).get(self.cell_alias)
        ):
            click.echo(
                click.style(
                    f"Error: Could not find the cell {self.cell_alias} in the canvas {self.canvas}.",
                    fg="red",
                )
            )
            raise ValueError(
                f"Could not find the cell {self.cell_alias} in the canvas {self.canvas}."
            )

        # Set up run directory
        self.runs_dir = os.path.normpath(
            os.path.join(
                ProjectConfig.RUNS_DIR,
                self.canvas if self.canvas else "",
                self.run_id,
            )
        )
        if not os.path.exists(self.runs_dir):
            os.makedirs(self.runs_dir)

        # Set up logger
        self.log_path = os.path.join(self.runs_dir, f"{self.cell_alias}.log")
        self.logger = get_morph_logger(self.log_path)

        # load .env in project root and set timezone
        dotenv_path = os.path.join(self.project_root, ".env")
        load_dotenv(dotenv_path)
        self.setup_code += self._load_env_from_cloud()
        if self.canvas:
            self.setup_code += f'os.environ["MORPH_CANVAS"] = "{self.canvas}"\n'
        desired_tz = os.getenv("TZ")
        if desired_tz is not None:
            tz_manager = TimezoneManager()
            if not tz_manager.is_valid_timezone(desired_tz):
                self.logger.error(f"Invalid TZ value in .env: {desired_tz}")
                raise ValueError(f"Invalid TZ value in .env: {desired_tz}")
            if desired_tz != tz_manager.get_current_timezone():
                tz_manager.change_timezone(desired_tz)

    def _save_morph_config(self) -> None:
        with open(self.project_config_path, "w") as file:
            yaml.safe_dump(self.morph_config.to_dict(), file, sort_keys=False)

    def _insert_run_record(self, cell_alias: str) -> None:
        status = "inProgress"
        started_at = datetime.now().isoformat()

        self.db_manager.insert_run_record(
            self.run_id,
            self.canvas,
            cell_alias,
            self.is_dag,
            status,
            started_at,
            self.log_path,
        )

    def _update_run_record(
        self,
        cell_alias: str,
        new_status: str,
        error: Optional[Union[str, dict]] = None,
        output_file: Optional[str] = None,
    ) -> None:
        if isinstance(error, dict):
            error = json.dumps(error, indent=None)
        self.db_manager.update_run_record(
            self.run_id, self.canvas, cell_alias, new_status, error, output_file
        )

    def run(self) -> None:
        if self.is_dry_run:
            if self.is_dag:
                execution_order = self.morph_config.get_dag_execution_order(
                    self.canvas, self.cell_alias
                )
            else:
                execution_order = [self.cell_alias]

            # Format execution order as a single line list
            execution_order_str = ", ".join(execution_order)
            self.logger.info(
                f"Dry run mode enabled. Following cells will be executed: [{execution_order_str}]"
            )
            return

        # NOTE: morphdb-utilsから相対参照できるようにカレントディレクトリを変更
        os.chdir(os.path.dirname(self.filename))
        if self.is_dag:
            self._run_dag()
        else:
            self._execute_cell(self.cell_alias)

    def _run_dag(self) -> None:
        execution_order = self.morph_config.get_dag_execution_order(
            self.canvas, self.cell_alias
        )
        for cell in execution_order:
            self._execute_cell(cell)

    def _execute_cell(self, cell: str) -> None:
        # Override cell_alias to the current cell
        self.cell_alias = cell
        self.log_path = os.path.join(self.runs_dir, f"{self.cell_alias}.log")
        self.logger = get_morph_logger(self.log_path)

        # Override output directory
        self.output_dir = os.path.join(
            self.project_root,
            "src",
            ProjectConfig.OUTPUTS_DIR,
            f"{ProjectPrefix.OUTPUTS_PREFIX}{self.cell_alias}",
        )
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self._insert_run_record(self.cell_alias)

        # Execute cell
        if self.ext == ".sql":
            self._run_sql(self.cell_alias)
        elif self.ext == ".py":
            self._run_python(self.cell_alias)
        else:
            text = "Invalid file type. Please specify a .sql or .py file."
            self.logger.error(text)
            self._update_run_record(
                self.cell_alias, RunStatus.FAILED, {"error": "Invalid file type"}
            )

    def _run_sql(self, cell: str) -> None:
        self.logger.info(f"Running sql file: {self.filename}")

        try:
            output_file = os.path.join(self.output_dir, f"{self.output_filename}.csv")
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            url = f"{self.app_url}/{self.database_id}/sql/python"
            headers = {
                "x-api-key": self.api_key,
            }
            code = open(self.filename, "r").read()
            request = {"sql": code}
            resource = self.morph_config.resources.get(self.cell_alias)
            connection = resource.get("connection")
            if connection is not None:
                request["connectionSlug"] = connection

            response = requests.post(
                url=url, headers=headers, json=request, verify=True
            )
            if response.status_code > 500:
                text = f"An error occurred while running the SQL: {response.text}"
                self.logger.error(text)
                self._update_run_record(cell, RunStatus.FAILED, {"error": text})
                return
            else:
                response_json = response.json()
                if (
                    "error" in response_json
                    and "subCode" in response_json
                    and "message" in response_json
                ):
                    error_message = response_json["message"]
                    text = f"An error occurred while running the SQL: {error_message}"
                    self.logger.error(text)
                    self._update_run_record(cell, RunStatus.FAILED, {"error": text})
                    return
                else:
                    structured_response = SqlResultResponse(
                        headers=response_json["headers"], rows=response_json["rows"]
                    )
                    df = convert_sql_response(structured_response)
                    output = df.to_csv()

                    with open(output_file, "w") as f:
                        f.write(output)
                    self.logger.info(f"Cell output saved to: {output_file}")
                    self._update_run_record(cell, RunStatus.DONE, None, output_file)
        except Exception as e:
            text = f"An error occurred while running the SQL: {str(e)}"
            self.logger.error(text)
            self._update_run_record(cell, RunStatus.FAILED, {"error": text})
            return

        self.logger.info(f"Successfully ran sql file: {self.filename}")

    def _run_python(self, cell: str) -> None:
        self.logger.info(f"Running python file: {self.filename}")

        try:
            timeout_seconds = -1
            code = open(self.filename, "r").read()
            debug = False
            decorator_name = None
            decorators = DecoratorParser.get_decorators(code)
            for decorator in decorators:
                if isinstance(decorator, dict):
                    decorator_name = decorator.get("name")
                else:
                    decorator_name = decorator

            try:
                result, error, profiler, code = run_with_timeout(
                    execute_user_code,
                    timeout_seconds,
                    args=(code, self.setup_code, debug, self.logger),
                )
            except TimeoutException:
                text = (
                    f"Timeout error occurred while running the script: {self.filename}"
                )
                self.logger.error(text)
                self._update_run_record(cell, RunStatus.FAILED, {"error": "Timeout"})
                return
            except Exception as e:
                text = f"An error occurred while running the script: {str(e)}"
                self.logger.error(text)
                self._update_run_record(cell, RunStatus.FAILED, {"error": text})
                return

            if error is not None:
                text = f"An error occurred while running the script: {error}"
                self.logger.error(text)
                self._update_run_record(cell, RunStatus.FAILED, error)
                return

            # NOTE: morphdb-utilsのデコレータから値を受け取る場合はここで処理する
            # if isinstance(result, Tuple):
            #     result, extras = result

            if decorator_name == "visualize":
                if isinstance(result, list):
                    output = result[0]
                else:
                    output = str(result)
                output_file = os.path.join(
                    self.output_dir,
                    f"{self.output_filename}.html",
                )
            elif decorator_name == "transform":
                if isinstance(result, pd.DataFrame):
                    output = result.to_csv()
                else:
                    output = str(result)
                output_file = os.path.join(
                    self.output_dir,
                    f"{self.output_filename}.csv",
                )
            elif decorator_name == "report":
                if isinstance(result, pd.DataFrame):
                    output = result.to_string()
                else:
                    output = str(result)
                output_file = os.path.join(
                    self.output_dir,
                    f"{self.output_filename}.md",
                )
            else:
                if isinstance(result, pd.DataFrame):
                    output = result.to_string()
                else:
                    output = str(result)
                output_file = os.path.join(
                    self.output_dir,
                    f"{self.output_filename}.txt",
                )

            if output_file:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(output_file, "w") as f:
                    f.write(output)
                self.logger.info(f"Cell output saved to: {output_file}")

            self._update_run_record(cell, RunStatus.DONE, None, output_file)

        except Exception as e:
            text = f"An error occurred while running the script: {str(e)}"
            self.logger.error(text)
            self._update_run_record(cell, RunStatus.FAILED, {"error": text})
            return

        self.logger.info(f"Successfully ran python file: {self.filename}")

    def _load_env_from_cloud(self):
        url = f"{self.app_url}/{self.database_id}/env-vars"
        headers = {
            "x-api-key": self.api_key,
        }
        try:
            response = requests.get(url=url, headers=headers, verify=True)
            if response.status_code > 500:
                self.logger.error(
                    f"An error occurred while loading environment variables: {response.text}"
                )
                return ""
            else:
                response_json = response.json()
                if (
                    "error" in response_json
                    and "subCode" in response_json
                    and "message" in response_json
                ):
                    self.logger.error(
                        f"An error occurred while loading environment variables: {response_json['message']}"
                    )
                    return ""
                else:
                    env_vars = ""
                    for item in response_json["items"]:
                        key = item["key"]
                        value = item["value"]
                        env_vars += f'os.environ["{key}"] = "{value}"\n'
                    return env_vars
        except Exception as e:
            self.logger.error(
                f"An error occurred while loading environment variables: {str(e)}"
            )
            return ""
