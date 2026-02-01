from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Callable, Iterable, TypeVar, Union

if TYPE_CHECKING:
    from stdlibx.itertools._types import Operation

T = TypeVar("T")
U = TypeVar("U")


def map_(
    func: Callable[[T], U], /, *, lazy: bool = True
) -> Operation[Iterable[T], Iterable[U]]:
    def _execute(iterable: Iterable[T]) -> Iterable[U]:
        if lazy:
            return map(func, iterable)
        return [func(a) for a in iterable]

    return _execute


def filter_(
    func: Callable[[T], bool], /, *, lazy: bool = True
) -> Operation[Iterable[T], Iterable[T]]:
    def _execute(iterable: Iterable[T]) -> Iterable[T]:
        if lazy:
            return filter(func, iterable)
        return [a for a in iterable if func(a)]

    return _execute


def filter_none(
    *, lazy: bool = True
) -> Operation[Iterable[Union[T, None]], Iterable[T]]:
    def _execute(iterable: Iterable[Union[T, None]]) -> Iterable[T]:
        if lazy:
            return (a for a in iterable if a is not None)
        return [a for a in iterable if a is not None]

    return _execute


def reduce(initial: T, func: Callable[[T, U], T]) -> Operation[Iterable[U], T]:
    def _execute(iterable: Iterable[U]) -> T:
        return functools.reduce(func, iterable, initial)

    return _execute


def collect() -> Operation[Iterable[T], list[T]]:
    return reduce([], lambda a, b: a + [b])
