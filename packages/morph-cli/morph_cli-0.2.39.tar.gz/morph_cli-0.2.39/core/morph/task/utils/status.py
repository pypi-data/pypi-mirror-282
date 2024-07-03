import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class RunStatus(str, Enum):
    DONE = "done"
    TIMEOUT = "timeout"
    UNEXPECTED = "unexpected"
    IN_PROGRESS = "inProgress"
    FAILED = "failed"


@dataclass
class CellResult:
    cell: str
    status: RunStatus
    error: Optional[str]
    startedAt: str
    endedAt: Optional[str]
    log: str
    result: str


@dataclass
class StatusJson:
    runId: str
    cells: List[CellResult] = field(default_factory=list)
    status: RunStatus = RunStatus.IN_PROGRESS
    error: Optional[str] = None
    startedAt: str = field(default_factory=lambda: datetime.now().isoformat())
    endedAt: Optional[str] = None

    def to_dict(self):
        return {
            "runId": self.runId,
            "cells": [cell.__dict__ for cell in self.cells],
            "status": self.status.value,
            "error": self.error,
            "startedAt": self.startedAt,
            "endedAt": self.endedAt,
        }

    @staticmethod
    def from_dict(data: dict):
        cells = [CellResult(**cell) for cell in data["cells"]]
        return StatusJson(
            runId=data["runId"],
            cells=cells,
            status=RunStatus(data["status"]),
            error=data.get("error"),
            startedAt=data["startedAt"],
            endedAt=data.get("endedAt"),
        )

    @classmethod
    def read(cls, file_path: str):
        with open(file_path, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)

    def write(self, file_path: str):
        with open(file_path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    def update(self, updates: Dict):
        for key, value in updates.items():
            if hasattr(self, key):
                if key == "status":
                    value = RunStatus(value)
                setattr(self, key, value)
            else:
                raise KeyError(f"Key {key} not found in StatusJson")

    @classmethod
    def delete(cls, file_path: str):
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"No such file: '{file_path}'")
