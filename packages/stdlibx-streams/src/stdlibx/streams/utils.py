from __future__ import annotations

from typing import TypeVar

from stdlibx.streams._subject import Subject
from stdlibx.streams._types import Observable

T = TypeVar("T")


def as_observable(value: Observable[T] | T) -> Observable[T]:
    if isinstance(value, Observable):
        return value
    return Subject(value)
