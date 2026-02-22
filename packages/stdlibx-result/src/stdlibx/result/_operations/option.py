from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from stdlibx.result import methods

if TYPE_CHECKING:
    from stdlibx.option.types import Option
    from stdlibx.result.types import Operation, Result

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")


def get_ok() -> Operation[Result[T, E], Option[T]]:
    return methods.get_ok


def get_error() -> Operation[Result[T, E], Option[E]]:
    return methods.get_error


def transpose() -> Operation[Result[Option[U], E], Option[Result[U, E]]]:
    return methods.transpose
