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
def pipe(a: Operation[T1, T2], b: Operation[T2, T3], /) -> Operation[T1, T3]: ...


@overload
def pipe(
    a: Operation[T1, T2], b: Operation[T2, T3], c: Operation[T3, T4], /
) -> Operation[T1, T4]: ...


@overload
def pipe(
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    /,
) -> Operation[T1, T5]: ...


@overload
def pipe(
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    /,
) -> Operation[T1, T6]: ...


@overload
def pipe(
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    f: Operation[T6, T7],
    /,
) -> Operation[T1, T7]: ...


@overload
def pipe(
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    f: Operation[T6, T7],
    g: Operation[T7, T8],
    /,
) -> Operation[T1, T8]: ...


@overload
def pipe(
    a: Operation[T1, T2],
    b: Operation[T2, T3],
    c: Operation[T3, T4],
    d: Operation[T4, T5],
    e: Operation[T5, T6],
    f: Operation[T6, T7],
    g: Operation[T7, T8],
    h: Operation[T9, T9],
    /,
) -> Operation[T1, T9]: ...


def pipe(
    first: Operation[Any, Any],
    *others: Operation[Any, Any],
) -> Operation[Any, Any]:
    def _apply(value: Any) -> Any:
        return functools.reduce(
            lambda val, operation: operation(val),
            (first, *others),
            value,
        )

    return _apply
