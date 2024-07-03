import functools

import click

from morph.cli import params, requires
from morph.task.file import DeleteFileTask


def global_flags(func):
    @params.log_format
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
    epilog="Specify one of these sub-commands and you can find more help from there.",
)
@click.pass_context
@global_flags
def cli(ctx, **kwargs):
    """An data analysis tool for SQL transformations, visualization, and reporting.
    For more information on these commands, visit: docs.morphdb.io
    """


@cli.command("init")
@click.pass_context
@global_flags
@requires.preflight
@requires.postflight
def init(ctx, **kwargs):
    from morph.task.init import InitTask

    task = InitTask(ctx.obj["flags"])
    results = task.run()
    return results, True


@cli.command("new")
@click.argument("directory_name", required=True)
@click.pass_context
@global_flags
@requires.preflight
@requires.postflight
def new(ctx, directory_name, **kwargs):
    from morph.task.new import NewTask

    task = NewTask(ctx.obj["flags"], directory_name)
    results = task.run()
    return results, True


@cli.command("run")
@click.argument("filename", required=True)
@click.argument("run_id", required=False, type=str)
@click.pass_context
@global_flags
@params.canvas
@params.dag
@params.dry_run
@requires.preflight
@requires.postflight
def run(ctx, **kwargs):
    """Run sql and python file and bring the results in output file."""
    from morph.task.run import RunTask

    task = RunTask(ctx.obj["flags"])
    results = task.run()
    return results, True


@cli.command("create-file")
@click.argument("filename", required=True, type=str)
@click.argument("content", required=False, type=str, default=None)
@click.pass_context
@global_flags
@params.dag
@requires.preflight
@requires.postflight
def create_file(ctx, **kwargs):
    """Create a file with specified file type."""
    from morph.task.file import CreateFileTask

    task = CreateFileTask(ctx.obj["flags"])
    results = task.run()
    return results, True


@cli.command("update-file")
@click.argument("filename", required=True, type=str)
@click.argument("content", required=True, type=str)
@click.pass_context
@global_flags
@params.dag
@requires.preflight
@requires.postflight
def update_file(ctx, **kwargs):
    """Update a file content."""
    from morph.task.file import UpdateFileTask

    task = UpdateFileTask(ctx.obj["flags"])
    results = task.run()
    return results, True


@cli.command("delete-file")
@click.argument("filename", required=True, type=str)
@click.pass_context
@global_flags
@params.dag
@requires.preflight
@requires.postflight
def delete_file(ctx, **kwargs):
    """Delete a file."""

    task = DeleteFileTask(ctx.obj["flags"])
    results = task.run()
    return results, True


@cli.command("print")
@click.option("--path", type=str, help="Resource path to print details for.")
@click.option("--alias", type=str, help="Resource alias to print details for.")
@click.pass_context
@global_flags
@requires.preflight
@requires.postflight
def print_resource(ctx, path, alias, **kwargs):
    """Print details for the specified resource by path or alias."""
    """Print resource details by alias or path."""
    from morph.task.print import PrintResourceTask

    task = PrintResourceTask(ctx.obj["flags"])
    results = task.run()
    return results, True


@cli.command("sync")
@click.pass_context
@global_flags
@requires.preflight
@requires.postflight
def sync(ctx, **kwargs):
    """Sync resources from morph.yaml to the SQLite database."""
    from morph.task.sync import SyncTask

    task = SyncTask(ctx.obj["flags"])
    results = task.run()
    return results, True


if __name__ == "__main__":
    cli()
