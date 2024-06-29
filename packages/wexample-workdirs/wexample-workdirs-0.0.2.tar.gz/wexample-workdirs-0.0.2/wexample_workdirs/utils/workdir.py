from __future__ import annotations
from pydantic import BaseModel

from wexample_filestate.file_state_manager import FileStateManager
from wexample_helpers.const.types import FileStringOrPath


class WorkDir(BaseModel):
    _state_manager: FileStateManager
    path: FileStateManager

    def __init__(self, path: FileStringOrPath):
        super().__init__(path=path)

        self._state_manager = FileStateManager(path)

