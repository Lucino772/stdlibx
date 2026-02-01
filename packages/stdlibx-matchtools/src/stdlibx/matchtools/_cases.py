from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, TypeVar, Union, overload

from typing_extensions import TypeAlias, TypeGuard

if TYPE_CHECKING:
    from stdlibx.matchtools._types import Operation

T = TypeVar("T")
U = TypeVar("U")

T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T6 = TypeVar("T6")
T7 = TypeVar("T7")
T8 = TypeVar("T8")
T9 = TypeVar("T9")

U1 = TypeVar("U1")
U2 = TypeVar("U2")
U3 = TypeVar("U3")
U4 = TypeVar("U4")
U5 = TypeVar("U5")
U6 = TypeVar("U6")
U7 = TypeVar("U7")
U8 = TypeVar("U8")
U9 = TypeVar("U9")


Case: TypeAlias = tuple[Callable[[Any], TypeGuard[T]], Callable[[T], U]]


def type_is(type_: type[T], func: Callable[[T], U]) -> Case[T, U]:
    return (lambda val: isinstance(val, type_), func)  # type: ignore


@overload
def cases(
    a: Case[T1, U1], b: Case[T2, U2], /
) -> Operation[Union[T1, T2], Union[U1, U2]]: ...


@overload
def cases(
    a: Case[T1, U1], b: Case[T2, U2], c: Case[T3, U3], /
) -> Operation[Union[T1, T2, T3], Union[U1, U2, U3]]: ...


@overload
def cases(
    a: Case[T1, U1], b: Case[T2, U2], c: Case[T3, U3], d: Case[T4, U4], /
) -> Operation[Union[T1, T2, T3, T4], Union[U1, U2, U3, U4]]: ...


@overload
def cases(
    a: Case[T1, U1],
    b: Case[T2, U2],
    c: Case[T3, U3],
    d: Case[T4, U4],
    e: Case[T5, U5],
    /,
) -> Operation[Union[T1, T2, T3, T4, T5], Union[U1, U2, U3, U4, U5]]: ...


@overload
def cases(
    a: Case[T1, U1],
    b: Case[T2, U2],
    c: Case[T3, U3],
    d: Case[T4, U4],
    e: Case[T5, U5],
    f: Case[T6, U6],
    /,
) -> Operation[Union[T1, T2, T3, T4, T5, T6], Union[U1, U2, U3, U4, U5, U6]]: ...


@overload
def cases(
    a: Case[T1, U1],
    b: Case[T2, U2],
    c: Case[T3, U3],
    d: Case[T4, U4],
    e: Case[T5, U5],
    f: Case[T6, U6],
    g: Case[T7, U7],
    /,
) -> Operation[
    Union[T1, T2, T3, T4, T5, T6, T7],
    Union[U1, U2, U3, U4, U5, U6, U7],
]: ...


@overload
def cases(
    a: Case[T1, U1],
    b: Case[T2, U2],
    c: Case[T3, U3],
    d: Case[T4, U4],
    e: Case[T5, U5],
    f: Case[T6, U6],
    g: Case[T7, U7],
    h: Case[T8, U8],
    /,
) -> Operation[
    Union[T1, T2, T3, T4, T5, T6, T7, T8],
    Union[U1, U2, U3, U4, U5, U6, U7, U8],
]: ...


@overload
def cases(
    a: Case[T1, U1],
    b: Case[T2, U2],
    c: Case[T3, U3],
    d: Case[T4, U4],
    e: Case[T5, U5],
    f: Case[T6, U6],
    g: Case[T7, U7],
    h: Case[T8, U8],
    i: Case[T9, U9],
    /,
) -> Operation[
    Union[T1, T2, T3, T4, T5, T6, T7, T8, T9],
    Union[U1, U2, U3, U4, U5, U6, U7, U8, U9],
]: ...


def cases(*conditions: Case[Any, Any]) -> Operation[Any, Any]:
    def _execute(value: Any) -> Any:
        for condition, op in conditions:
            if condition(value) is True:
                return op(value)

        msg = "Failed to handle all cases, make sure to include a catch-all case"
        raise RuntimeError(msg)

    return _execute
