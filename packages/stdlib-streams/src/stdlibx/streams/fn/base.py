from __future__ import annotations

import operator
from functools import partial
from typing import (
    TYPE_CHECKING,
    TypeVar,
    Union,
)

from stdlibx.streams import methods
from typing_extensions import TypeGuard, TypeVarTuple, Unpack

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

    from stdlibx.streams._types import (
        Observable,
        Operation,
    )

T = TypeVar("T")
U = TypeVar("U")
Ts = TypeVarTuple("Ts")


def map_(func: Callable[[T], U]) -> Operation[Observable[T], Observable[U]]:
    return partial(methods.map_, func=func)


def if_(func: Callable[[T], bool]) -> Operation[Observable[T], Observable[T]]:
    return partial(methods.if_, func=func)


def is_(
    func: Callable[[Union[T, U]], TypeGuard[U]],
) -> Operation[Observable[Union[T, U]], Observable[U]]:
    return partial(methods.is_, func=func)


def is_not_none() -> Operation[Observable[Union[T, None]], Observable[T]]:
    return methods.is_not_none


def as_tuple() -> Operation[Observable[T], Observable[tuple[T]]]:
    return methods.as_tuple


def combine(
    other: Observable[U],
) -> Operation[Observable[tuple[Unpack[Ts]]], Observable[tuple[Unpack[Ts], U]]]:
    return partial(methods.combine, other=other)


def start_with(value: T) -> Operation[Observable[T], Observable[T]]:
    return partial(methods.start_with, value=value)


def for_(
    func: Callable[[T], U],
) -> Operation[Observable[Iterable[T]], Observable[Iterable[U]]]:
    return partial(methods.for_, func=func)


def distinct(
    equal_fn: Callable[[T, T], bool] = operator.eq,
) -> Operation[Observable[T], Observable[T]]:
    return partial(methods.distinct, equal_fn=equal_fn)
