from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, Iterable, TypeVar, overload

from stdlibx.option._option import is_some, nothing, some

if TYPE_CHECKING:
    from stdlibx.option.types import Option

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T6 = TypeVar("T6")
T7 = TypeVar("T7")
T8 = TypeVar("T8")
T9 = TypeVar("T9")


@overload
def collect(a: Option[T1], b: Option[T2], /) -> Option[tuple[T1, T2]]: ...


@overload
def collect(
    a: Option[T1], b: Option[T2], c: Option[T3], /
) -> Option[tuple[T1, T2, T3]]: ...


@overload
def collect(
    a: Option[T1], b: Option[T2], c: Option[T3], d: Option[T4], /
) -> Option[tuple[T1, T2, T3, T4]]: ...


@overload
def collect(
    a: Option[T1], b: Option[T2], c: Option[T3], d: Option[T4], e: Option[T5], /
) -> Option[tuple[T1, T2, T3, T4, T5]]: ...


@overload
def collect(
    a: Option[T1],
    b: Option[T2],
    c: Option[T3],
    d: Option[T4],
    e: Option[T5],
    f: Option[T6],
    /,
) -> Option[tuple[T1, T2, T3, T4, T5, T6]]: ...


@overload
def collect(
    a: Option[T1],
    b: Option[T2],
    c: Option[T3],
    d: Option[T4],
    e: Option[T5],
    f: Option[T6],
    g: Option[T7],
    /,
) -> Option[tuple[T1, T2, T3, T4, T5, T6, T7]]: ...


@overload
def collect(
    a: Option[T1],
    b: Option[T2],
    c: Option[T3],
    d: Option[T4],
    e: Option[T5],
    f: Option[T6],
    g: Option[T7],
    h: Option[T8],
    /,
) -> Option[tuple[T1, T2, T3, T4, T5, T6, T7, T8]]: ...


@overload
def collect(
    a: Option[T1],
    b: Option[T2],
    c: Option[T3],
    d: Option[T4],
    e: Option[T5],
    f: Option[T6],
    g: Option[T7],
    h: Option[T8],
    i: Option[T9],
    /,
) -> Option[tuple[T1, T2, T3, T4, T5, T6, T7, T8, T9]]: ...


def collect(initial: Option[Any], *others: Option[Any]) -> Option[tuple[Any, ...]]:
    def _combine(a: Option[tuple[Any, ...]], b: Option[Any]) -> Option[tuple[Any, ...]]:
        if is_some(a) and is_some(b):
            return some(((*a.value, b.value)))
        return nothing()

    return functools.reduce(_combine, [initial, *others], some(()))


def collect_all(iterable: Iterable[Option[T]]) -> Option[tuple[T, ...]]:
    def _combine(a: Option[tuple[T, ...]], b: Option[T]) -> Option[tuple[T, ...]]:
        if is_some(a) and is_some(b):
            return some(((*a.value, b.value)))
        return nothing()

    return functools.reduce(_combine, iterable, some(()))
