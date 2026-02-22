from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from stdlibx import option
from stdlibx.result._result import error, is_err, is_ok, ok

if TYPE_CHECKING:
    from stdlibx.option.types import Option
    from stdlibx.result.types import Result

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")


def get_ok(result: Result[T, E]) -> Option[T]:
    if is_ok(result):
        return option.some(result.value)
    return option.nothing()


def get_error(result: Result[T, E]) -> Option[E]:
    if is_err(result):
        return option.some(result.error)
    return option.nothing()


def transpose(result: Result[Option[U], E]) -> Option[Result[U, E]]:
    if is_ok(result) and option.is_some(result.value):
        return option.some(ok(result.value.value))
    elif is_err(result):
        return option.some(error(result.error))
    else:
        return option.nothing()
