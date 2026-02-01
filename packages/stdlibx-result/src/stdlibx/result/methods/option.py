from __future__ import annotations

from typing import TypeVar

from stdlibx.option import Nothing, Option, Some, is_some
from stdlibx.result._result import Error, Ok, Result, is_err, is_ok

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")


def ok(result: Result[T, E]) -> Option[T]:
    if is_ok(result):
        return Some(result.value)
    return Nothing()


def err(result: Result[T, E]) -> Option[E]:
    if is_err(result):
        return Some(result.error)
    return Nothing()


def transpose(result: Result[Option[U], E]) -> Option[Result[U, E]]:
    if is_ok(result) and is_some(result.value):
        return Some(Ok(result.value.value))
    elif is_err(result):
        return Some(Error(result.error))
    else:
        return Nothing()
