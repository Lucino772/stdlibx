from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, TypeVar, overload

if TYPE_CHECKING:
    from stdlibx.compose._types import Operation

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
def flow(source: T1, a: Operation[T1, T2], /) -> T2: ...


@overload
def flow(source: T1, a: Operation[T1, T2], b: Operation[T2, T3], /) -> T3: ...


@overload
def flow(
    source: T1, a: Operation[T1, T2], b: Operation[T2, T3], c: Operation[T3, T4], /
) -> T4: ...


@overload
def flow(
    source: T1,
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    /,
) -> T5: ...


@overload
def flow(
    source: T1,
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    /,
) -> T6: ...


@overload
def flow(
    source: T1,
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    f: Operation[T6, T7],
    /,
) -> T7: ...


@overload
def flow(
    source: T1,
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    f: Operation[T6, T7],
    g: Operation[T7, T8],
    /,
) -> T8: ...


@overload
def flow(
    source: T1,
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    f: Operation[T6, T7],
    g: Operation[T7, T8],
    h: Operation[T8, T9],
    /,
) -> T9: ...


def flow(source: Any, *operations: Operation[Any, Any]) -> Any:
    return functools.reduce(lambda val, operator: operator(val), operations, source)
