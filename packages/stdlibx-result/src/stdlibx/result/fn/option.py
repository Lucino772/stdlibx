from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from stdlibx.result import Result, methods

if TYPE_CHECKING:
    from stdlibx.option import Option
    from stdlibx.result._types import Operation

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")


def ok() -> Operation[Result[T, E], Option[T]]:
    return methods.ok


def err() -> Operation[Result[T, E], Option[E]]:
    return methods.err


def transpose() -> Operation[Result[Option[U], E], Option[Result[U, E]]]:
    return methods.transpose
