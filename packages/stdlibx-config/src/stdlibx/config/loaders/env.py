from __future__ import annotations

import os
from typing import Any, Mapping


class EnvLoader:
    def __init__(
        self,
        environ: Mapping[str, str] | None = None,
        env_prefix: str = "STDLIBX_",
        env_nested_delimiter: str = "__",
    ) -> None:
        self.__environ = environ
        self.__env_prefix = env_prefix
        self.__env_nested_delimiter = env_nested_delimiter

    def load(self) -> Mapping[str, Any]:
        _environ = self.__environ or os.environ

        _ret = {}
        for key, value in (
            (key.upper().strip(self.__env_prefix + "_").lower(), value)
            for key, value in _environ.items()
            if key.upper().startswith(self.__env_prefix)
        ):
            if self.__env_nested_delimiter not in key:
                _ret[key] = value
            else:
                keys = key.split(self.__env_nested_delimiter)

                _value = _ret
                for _key in keys[:-1]:
                    if _key not in _value:
                        _value[_key] = {}
                    _value = _value[_key]
                _value[keys[-1]] = value

        return _ret
