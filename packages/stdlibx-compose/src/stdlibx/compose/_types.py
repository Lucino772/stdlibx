from __future__ import annotations

from typing import Callable, TypeVar

from typing_extensions import TypeAlias

T = TypeVar("T")
U = TypeVar("U")

Operation: TypeAlias = Callable[[T], U]
