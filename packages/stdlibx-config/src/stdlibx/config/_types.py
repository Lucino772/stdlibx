from collections.abc import Mapping
from typing import Any, Protocol, TypeVar

T = TypeVar("T", covariant=True)


class Loader(Protocol):
    def load(self) -> Mapping[str, Any]: ...


class SupportsRead(Protocol[T]):
    def read(self, length: int = ..., /) -> T: ...
