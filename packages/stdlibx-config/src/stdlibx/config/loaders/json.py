from __future__ import annotations

import json
from typing import TYPE_CHECKING

from stdlibx.config.loaders.file import FileLoader

if TYPE_CHECKING:
    from os import PathLike


class JsonLoader(FileLoader):
    def __init__(self, path: str | PathLike[str], *, missing_ok: bool = False) -> None:
        super().__init__(path, json.load, missing_ok=missing_ok)
