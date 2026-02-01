from __future__ import annotations

from typing import Callable, TypeVar

from stdlibx.option import (
    Nothing,
    Option,
    OptionExpectError,
    OptionUnwrapError,
    Some,
    is_none,
    is_some,
)
from typing_extensions import TypeVarTuple, Unpack

T = TypeVar("T")
U = TypeVar("U")
Ts = TypeVarTuple("Ts")


def is_some_and(opt: Option[T], func: Callable[[T], bool]) -> bool:
    return is_some(opt) and func(opt.value)


def is_none_or(opt: Option[T], func: Callable[[T], bool]) -> bool:
    return is_none(opt) or (is_some(opt) and func(opt.value))


def expect(opt: Option[T], msg: str) -> T:
    if is_some(opt):
        return opt.value
    raise OptionExpectError(msg)


def unwrap(opt: Option[T]) -> T:
    if is_some(opt):
        return opt.value
    raise OptionUnwrapError


def unwrap_or(opt: Option[T], default: T) -> T:
    if is_some(opt):
        return opt.value
    return default


def unwrap_or_else(opt: Option[T], func: Callable[[], T]) -> T:
    if is_some(opt):
        return opt.value
    return func()


def map_(opt: Option[T], func: Callable[[T], U]) -> Option[U]:
    if is_some(opt):
        return Some(func(opt.value))
    return Nothing()


def inspect(opt: Option[T], func: Callable[[T], None]) -> Option[T]:
    if is_some(opt):
        func(opt.value)
    return opt


def map_or(opt: Option[T], default: U, func: Callable[[T], U]) -> U:
    if is_some(opt):
        return func(opt.value)
    return default


def map_or_else(opt: Option[T], default: Callable[[], U], func: Callable[[T], U]) -> U:
    if is_some(opt):
        return func(opt.value)
    return default()


def and_(opt: Option[T], other: Option[U]) -> Option[U]:
    if is_some(opt):
        return other
    return Nothing()


def and_then(opt: Option[T], func: Callable[[T], Option[U]]) -> Option[U]:
    if is_some(opt):
        return func(opt.value)
    return Nothing()


def filter_(opt: Option[T], predicate: Callable[[T], bool]) -> Option[T]:
    if is_some(opt) and predicate(opt.value) is True:
        return Some(opt.value)
    return Nothing()


def or_(opt: Option[T], default: Option[T]) -> Option[T]:
    if is_some(opt):
        return Some(opt.value)
    return default


def or_else(opt: Option[T], default: Callable[[], Option[T]]) -> Option[T]:
    if is_some(opt):
        return Some(opt.value)
    return default()


def xor(opt: Option[T], other: Option[T]) -> Option[T]:
    if is_some(opt) and is_none(other):
        return Some(opt.value)
    elif is_some(other) and is_none(opt):
        return Some(other.value)
    else:
        return Nothing()


def flatten(opt: Option[Option[T]]) -> Option[T]:
    if is_some(opt):
        return opt.value
    return Nothing()


def zipped(
    opt: Option[tuple[Unpack[Ts]]], func: Callable[[Unpack[Ts]], Option[U]]
) -> Option[tuple[Unpack[Ts], U]]:
    if is_some(opt):
        return map_(func(*opt.value), lambda val: (*opt.value, val))
    return Nothing()
