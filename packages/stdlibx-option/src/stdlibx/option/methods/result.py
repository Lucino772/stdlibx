from __future__ import annotations

from typing import Callable, TypeVar

from stdlibx.option import Nothing, Option, Some, is_some
from stdlibx.result import Error, Ok, Result, is_err, is_ok

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E")


def ok_or(opt: Option[T], error: E) -> Result[T, E]:
    if is_some(opt):
        return Ok(opt.value)
    return Error(error)


def ok_or_else(opt: Option[T], error: Callable[[], E]) -> Result[T, E]:
    if is_some(opt):
        return Ok(opt.value)
    return Error(error())


def transpose(opt: Option[Result[U, E]]) -> Result[Option[U], E]:
    if is_some(opt) and is_ok(opt.value):
        return Ok(Some(opt.value.value))
    elif is_some(opt) and is_err(opt.value):
        return Error(opt.value.error)
    else:
        return Ok(Nothing())
