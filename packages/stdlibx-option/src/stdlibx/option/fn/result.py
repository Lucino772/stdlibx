from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Callable, TypeVar

from stdlibx.option import Option, methods

if TYPE_CHECKING:
    from stdlibx.option._option import Operation
    from stdlibx.result import Result

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E")


def ok_or(error: E) -> Operation[Option[T], Result[T, E]]:
    return partial(methods.ok_or, error=error)


def ok_or_else(error: Callable[[], E]) -> Operation[Option[T], Result[T, E]]:
    return partial(methods.ok_or_else, error=error)


def transpose() -> Operation[Option[Result[U, E]], Result[Option[U], E]]:
    return methods.transpose
