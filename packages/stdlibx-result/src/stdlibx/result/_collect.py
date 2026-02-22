from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, Iterable, TypeVar, Union, overload

from stdlibx.result._result import error, is_err, ok

if TYPE_CHECKING:
    from stdlibx.result.types import Result

T = TypeVar("T")
E = TypeVar("E")

T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T6 = TypeVar("T6")
T7 = TypeVar("T7")
T8 = TypeVar("T8")
T9 = TypeVar("T9")

E1 = TypeVar("E1")
E2 = TypeVar("E2")
E3 = TypeVar("E3")
E4 = TypeVar("E4")
E5 = TypeVar("E5")
E6 = TypeVar("E6")
E7 = TypeVar("E7")
E8 = TypeVar("E8")
E9 = TypeVar("E9")


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    /,
) -> Result[tuple[T1, T2], Union[E1, E2]]: ...


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    c: Result[T3, E3],
    /,
) -> Result[tuple[T1, T2, T3], Union[E1, E2, E3]]: ...


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    c: Result[T3, E3],
    d: Result[T4, E4],
    /,
) -> Result[tuple[T1, T2, T3, T4], Union[E1, E2, E3, E4]]: ...


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    c: Result[T3, E3],
    d: Result[T4, E4],
    e: Result[T5, E5],
    /,
) -> Result[tuple[T1, T2, T3, T4, T5], Union[E1, E2, E3, E4, E5]]: ...


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    c: Result[T3, E3],
    d: Result[T4, E4],
    e: Result[T5, E5],
    f: Result[T6, E6],
    /,
) -> Result[tuple[T1, T2, T3, T4, T5, T6], Union[E1, E2, E3, E4, E5, E6]]: ...


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    c: Result[T3, E3],
    d: Result[T4, E4],
    e: Result[T5, E5],
    f: Result[T6, E6],
    g: Result[T7, E7],
    /,
) -> Result[tuple[T1, T2, T3, T4, T5, T6, T7], Union[E1, E2, E3, E4, E5, E6, E7]]: ...


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    c: Result[T3, E3],
    d: Result[T4, E4],
    e: Result[T5, E5],
    f: Result[T6, E6],
    g: Result[T7, E7],
    h: Result[T8, E8],
    /,
) -> Result[
    tuple[T1, T2, T3, T4, T5, T6, T7, T8],
    Union[E1, E2, E3, E4, E5, E6, E7, E8],
]: ...


@overload
def collect(
    a: Result[T1, E1],
    b: Result[T2, E2],
    c: Result[T3, E3],
    d: Result[T4, E4],
    e: Result[T5, E5],
    f: Result[T6, E6],
    g: Result[T7, E7],
    h: Result[T8, E8],
    i: Result[T9, E9],
    /,
) -> Result[
    tuple[T1, T2, T3, T4, T5, T6, T7, T8, T9],
    Union[E1, E2, E3, E4, E5, E6, E7, E8, E9],
]: ...


def collect(
    initial: Result[Any, Any],
    *others: Result[Any, Any],
) -> Result[tuple[Any, ...], Any]:
    def _combine(
        a: Result[tuple[Any, ...], Any],
        b: Result[Any, Any],
    ) -> Result[tuple[Any, ...], Any]:
        if is_err(a):
            return error(a.error)
        elif is_err(b):
            return error(b.error)
        else:
            return ok(((*a.value, b.value)))  # type: ignore

    return functools.reduce(_combine, [initial, *others], ok(()))


def collect_all(iterable: Iterable[Result[T, E]]) -> Result[tuple[T, ...], E]:
    def _combine(
        a: Result[tuple[T, ...], E],
        b: Result[T, E],
    ) -> Result[tuple[T, ...], E]:
        if is_err(a):
            return error(a.error)
        elif is_err(b):
            return error(b.error)
        else:
            return ok(((*a.value, b.value)))  # type: ignore

    return functools.reduce(_combine, iterable, ok(()))
