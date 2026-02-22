from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Callable, TypeVar

from stdlibx.option import methods
from typing_extensions import TypeVarTuple, Unpack

if TYPE_CHECKING:
    from stdlibx.option.types import Operation, Option

T = TypeVar("T")
U = TypeVar("U")
Ts = TypeVarTuple("Ts")


def is_some_and(func: Callable[[T], bool]) -> Operation[Option[T], bool]:
    return partial(methods.is_some_and, func=func)


def is_none_or(func: Callable[[T], bool]) -> Operation[Option[T], bool]:
    return partial(methods.is_none_or, func=func)


def expect(msg: str) -> Operation[Option[T], T]:
    return partial(methods.expect, msg=msg)


def unwrap() -> Operation[Option[T], T]:
    return methods.unwrap


def unwrap_or(default: T) -> Operation[Option[T], T]:
    return partial(methods.unwrap_or, default=default)


def unwrap_or_else(func: Callable[[], T]) -> Operation[Option[T], T]:
    return partial(methods.unwrap_or_else, func=func)


def map_(func: Callable[[T], U]) -> Operation[Option[T], Option[U]]:
    return partial(methods.map_, func=func)


def inspect(func: Callable[[T], None]) -> Operation[Option[T], Option[T]]:
    return partial(methods.inspect, func=func)


def map_or(default: U, func: Callable[[T], U]) -> Operation[Option[T], U]:
    return partial(methods.map_or, default=default, func=func)


def map_or_else(
    default: Callable[[], U], func: Callable[[T], U]
) -> Operation[Option[T], U]:
    return partial(methods.map_or_else, default=default, func=func)


def and_(other: Option[U]) -> Operation[Option[T], Option[U]]:
    return partial(methods.and_, other=other)


def and_then(func: Callable[[T], Option[U]]) -> Operation[Option[T], Option[U]]:
    return partial(methods.and_then, func=func)


def filter_(predicate: Callable[[T], bool]) -> Operation[Option[T], Option[T]]:
    return partial(methods.filter_, predicate=predicate)


def or_(default: Option[T]) -> Operation[Option[T], Option[T]]:
    return partial(methods.or_, default=default)


def or_else(default: Callable[[], Option[T]]) -> Operation[Option[T], Option[T]]:
    return partial(methods.or_else, default=default)


def xor(other: Option[T]) -> Operation[Option[T], Option[T]]:
    return partial(methods.xor, other=other)


def flatten() -> Operation[Option[Option[T]], Option[T]]:
    return methods.flatten


def zipped(
    func: Callable[[Unpack[Ts]], Option[U]],
) -> Operation[Option[tuple[Unpack[Ts]]], Option[tuple[Unpack[Ts], U]]]:
    return partial(methods.zipped, func=func)
