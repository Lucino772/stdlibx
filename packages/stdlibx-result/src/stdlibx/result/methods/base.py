from __future__ import annotations

from typing import Callable, TypeVar, Union

from stdlibx.result._errors import ResultExpectError, ResultUnwrapError
from stdlibx.result._result import Error, Ok, Result, is_err, is_ok
from typing_extensions import TypeVarTuple, Unpack

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
F = TypeVar("F")
Ts = TypeVarTuple("Ts")
_AnyException = TypeVar("_AnyException", bound=Exception)


def is_ok_and(result: Result[T, E], func: Callable[[T], bool]) -> bool:
    return is_ok(result) and func(result.value)


def is_err_and(result: Result[T, E], func: Callable[[E], bool]) -> bool:
    return is_err(result) and func(result.error)


def map_(result: Result[T, E], func: Callable[[T], U]) -> Result[U, E]:
    if is_ok(result):
        return Ok(func(result.value))
    return Error(result.error)  # type: ignore


def map_or(result: Result[T, E], default: U, func: Callable[[T], U]) -> U:
    if is_ok(result):
        return func(result.value)
    return default


def map_or_else(
    result: Result[T, E], default: Callable[[E], U], func: Callable[[T], U]
) -> U:
    if is_ok(result):
        return func(result.value)
    return default(result.error)  # type: ignore


def map_err(result: Result[T, E], func: Callable[[E], F]) -> Result[T, F]:
    if is_err(result):
        return Error(func(result.error))
    return Ok(result.value)  # type: ignore


def inspect(result: Result[T, E], func: Callable[[T], None]) -> Result[T, E]:
    if is_ok(result):
        func(result.value)
    return result


def inspect_err(result: Result[T, E], func: Callable[[E], None]) -> Result[T, E]:
    if is_err(result):
        func(result.error)
    return result


def expect(result: Result[T, E], msg: str) -> T:
    if is_ok(result):
        return result.value

    _msg = f"{msg}: {result.error}"  # type: ignore
    raise ResultExpectError(_msg)


def unwrap(result: Result[T, E]) -> T:
    if is_ok(result):
        return result.value

    _msg = f"{result.error}"  # type: ignore
    raise ResultUnwrapError(_msg)


def expect_err(result: Result[T, E], msg: str) -> E:
    if is_err(result):
        return result.error

    _msg = f"{msg}: {result.value}"  # type: ignore
    raise ResultExpectError(_msg)


def unwrap_err(result: Result[T, E]) -> E:
    if is_err(result):
        return result.error

    _msg = f"{result.value}"  # type: ignore
    raise ResultUnwrapError(_msg)


def and_(result: Result[T, E], other: Result[U, F]) -> Result[U, Union[E, F]]:
    if is_ok(result):
        return other  # type: ignore
    return Error(result.error)  # type: ignore


def and_then(
    result: Result[T, E], func: Callable[[T], Result[U, F]]
) -> Result[U, Union[E, F]]:
    if is_ok(result):
        return func(result.value)  # type: ignore
    return Error(result.error)  # type: ignore


def or_(result: Result[T, E], default: Result[T, F]) -> Result[T, F]:
    if is_ok(result):
        return Ok(result.value)
    return default


def or_else(result: Result[T, E], default: Callable[[E], Result[T, F]]) -> Result[T, F]:
    if is_err(result):
        return default(result.error)
    return Ok(result.value)  # type: ignore


def unwrap_or(result: Result[T, E], default: T) -> T:
    if is_ok(result):
        return result.value
    return default


def unwrap_or_else(result: Result[T, E], default: Callable[[E], T]) -> T:
    if is_ok(result):
        return result.value
    return default(result.error)  # type: ignore


def unwrap_or_raise(result: Result[T, _AnyException]) -> T:
    if is_ok(result):
        return result.value
    raise result.error  # type: ignore


def flatten(result: Result[Result[T, E], F]) -> Result[T, Union[E, F]]:
    if is_ok(result):
        return result.value  # type: ignore
    return Error(result.error)  # type: ignore


def zipped(
    result: Result[tuple[Unpack[Ts]], E], func: Callable[[Unpack[Ts]], Result[U, E]]
) -> Result[tuple[Unpack[Ts], U], E]:
    if is_ok(result):
        return map_(func(*result.value), lambda val: (*result.value, val))
    return Error(result.error)  # type: ignore
