from __future__ import annotations

from typing import TYPE_CHECKING, Callable, TypeVar

from stdlibx import result
from stdlibx.option._option import is_some, nothing, some

if TYPE_CHECKING:
    from stdlibx.option.types import Option
    from stdlibx.result.types import Result

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E")


def ok_or(opt: Option[T], error: E) -> Result[T, E]:
    if is_some(opt):
        return result.ok(opt.value)
    return result.error(error)


def ok_or_else(opt: Option[T], error: Callable[[], E]) -> Result[T, E]:
    if is_some(opt):
        return result.ok(opt.value)
    return result.error(error())


def transpose(opt: Option[Result[U, E]]) -> Result[Option[U], E]:
    if is_some(opt) and result.is_ok(opt.value):
        return result.ok(some(opt.value.value))
    elif is_some(opt) and result.is_err(opt.value):
        return result.error(opt.value.error)
    else:
        return result.ok(nothing())
