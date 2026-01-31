from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Mapping

if TYPE_CHECKING:
    from os import PathLike

    from stdlibx.config._types import SupportsRead


class FileLoader:
    def __init__(
        self,
        path: str | PathLike[str],
        parser: Callable[[SupportsRead[bytes]], Mapping[str, Any]],
        *,
        missing_ok: bool = False,
    ) -> None:
        self.__path = Path(path)
        self.__missing_ok = missing_ok
        self.__parser = parser

    def load(self) -> Mapping[str, Any]:
        if self.__missing_ok is True and self.__path.exists() is False:
            return {}

        with open(self.__path, "rb") as fp:
            return self.__parser(fp)
