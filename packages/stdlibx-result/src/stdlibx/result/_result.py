from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, Callable, Generic, Literal, TypeVar

from stdlibx.result.types import Error, Ok
from typing_extensions import ParamSpec, TypeIs

if TYPE_CHECKING:
    from stdlibx.result.types import Operation, Result

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
P = ParamSpec("P")


def ok(value: T) -> Result[T, E]:
    return _Ok(value)


def error(error: E) -> Result[T, E]:
    return _Error(error)


def is_ok(result: Result[T, E]) -> TypeIs[Ok[T]]:
    return result.is_ok()


def is_err(result: Result[T, E]) -> TypeIs[Error[E]]:
    return result.is_err()


def try_(
    func: Callable[P, T], *args: P.args, **kwargs: P.kwargs
) -> Result[T, Exception]:
    try:
        return ok(func(*args, **kwargs))
    except Exception as e:
        return error(e)


def safe(func: Callable[P, T]) -> Callable[P, Result[T, Exception]]:
    @wraps(func)
    def _wrapped(*args: P.args, **kwargs: P.kwargs) -> Result[T, Exception]:
        try:
            return ok(func(*args, **kwargs))
        except Exception as e:
            return error(e)

    return _wrapped


class _Ok(Generic[T]):
    __match_args__ = ("value",)
    __slots__ = ("value",)

    value: T

    def __init__(self, value: T) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Ok({self.value!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Ok):
            return other.value == self.value
        return False

    def is_ok(self) -> Literal[True]:
        return True

    def is_err(self) -> Literal[False]:
        return False

    def apply(self, operation: Operation[Result[T, E], U]) -> U:
        return operation(self)


class _Error(Generic[E]):
    __match_args__ = ("error",)
    __slots__ = ("error",)

    error: E

    def __init__(self, error: E) -> None:
        self.error = error

    def __repr__(self) -> str:
        return f"Error({self.error!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Error):
            return other.error == self.error
        return False

    def is_ok(self) -> Literal[False]:
        return False

    def is_err(self) -> Literal[True]:
        return True

    def apply(self, operation: Operation[Result[T, E], U]) -> U:
        return operation(self)
