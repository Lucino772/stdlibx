from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from ruamel.yaml import YAML
from stdlibx.config.loaders.file import FileLoader

if TYPE_CHECKING:
    from os import PathLike


class YamlLoader(FileLoader):
    def __init__(
        self,
        path: str | PathLike[str],
        *,
        missing_ok: bool = False,
        yaml_typ: Literal["rt", "safe", "unsafe", "full", "base"] | None = None,
        yaml_pure: bool = False,
    ) -> None:
        super().__init__(
            path, YAML(typ=yaml_typ, pure=yaml_pure).load, missing_ok=missing_ok
        )
