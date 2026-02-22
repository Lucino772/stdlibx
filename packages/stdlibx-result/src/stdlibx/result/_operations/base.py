from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Callable, TypeVar, Union

from stdlibx.result import methods
from typing_extensions import TypeVarTuple, Unpack

if TYPE_CHECKING:
    from stdlibx.result.types import Operation, Result

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
F = TypeVar("F")
Ts = TypeVarTuple("Ts")
_AnyException = TypeVar("_AnyException", bound=Exception)


def is_ok_and(func: Callable[[T], bool]) -> Operation[Result[T, E], bool]:
    return partial(methods.is_ok_and, func=func)


def is_err_and(func: Callable[[E], bool]) -> Operation[Result[T, E], bool]:
    return partial(methods.is_err_and, func=func)


def map_(func: Callable[[T], U]) -> Operation[Result[T, E], Result[U, E]]:
    return partial(methods.map_, func=func)


def map_or(default: U, func: Callable[[T], U]) -> Operation[Result[T, E], U]:
    return partial(methods.map_or, default=default, func=func)


def map_or_else(
    default: Callable[[E], U], func: Callable[[T], U]
) -> Operation[Result[T, E], U]:
    return partial(methods.map_or_else, default=default, func=func)


def map_err(func: Callable[[E], F]) -> Operation[Result[T, E], Result[T, F]]:
    return partial(methods.map_err, func=func)


def inspect(func: Callable[[T], None]) -> Operation[Result[T, E], Result[T, E]]:
    return partial(methods.inspect, func=func)


def inspect_err(func: Callable[[E], None]) -> Operation[Result[T, E], Result[T, E]]:
    return partial(methods.inspect_err, func=func)


def expect(msg: str) -> Operation[Result[T, E], T]:
    return partial(methods.expect, msg=msg)


def unwrap() -> Operation[Result[T, E], T]:
    return methods.unwrap


def expect_err(msg: str) -> Operation[Result[T, E], E]:
    return partial(methods.expect_err, msg=msg)


def unwrap_err() -> Operation[Result[T, E], E]:
    return methods.unwrap_err


def and_(other: Result[U, F]) -> Operation[Result[T, E], Result[U, Union[E, F]]]:
    return partial(methods.and_, other=other)


def and_then(
    func: Callable[[T], Result[U, F]],
) -> Operation[Result[T, E], Result[U, Union[E, F]]]:
    return partial(methods.and_then, func=func)


def or_(default: Result[T, F]) -> Operation[Result[T, E], Result[T, F]]:
    return partial(methods.or_, default=default)


def or_else(
    default: Callable[[E], Result[T, F]],
) -> Operation[Result[T, E], Result[T, F]]:
    return partial(methods.or_else, default=default)


def unwrap_or(default: T) -> Operation[Result[T, E], T]:
    return partial(methods.unwrap_or, default=default)


def unwrap_or_else(default: Callable[[E], T]) -> Operation[Result[T, E], T]:
    return partial(methods.unwrap_or_else, default=default)


def unwrap_or_raise() -> Operation[Result[T, _AnyException], T]:
    return methods.unwrap_or_raise


def flatten() -> Operation[Result[Result[T, E], F], Result[T, Union[E, F]]]:
    return methods.flatten


def zipped(
    func: Callable[[Unpack[Ts]], Result[U, E]],
) -> Operation[Result[tuple[Unpack[Ts]], E], Result[tuple[Unpack[Ts], U], E]]:
    return partial(methods.zipped, func=func)
