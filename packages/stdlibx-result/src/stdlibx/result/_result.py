from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, Callable, Generic, Literal, TypeVar

from typing_extensions import ParamSpec, TypeAlias, TypeGuard

if TYPE_CHECKING:
    from stdlibx.result._types import Operation

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
P = ParamSpec("P")
_AnyException = TypeVar("_AnyException", bound=Exception)

Result: TypeAlias = "Ok[T, E] | Error[T, E]"


def is_ok(result: Result[T, E]) -> TypeGuard[Ok[T, E]]:
    return result.is_ok()


def is_err(result: Result[T, E]) -> TypeGuard[Error[T, E]]:
    return result.is_err()


def result_of(
    func: Callable[P, T], *args: P.args, **kwargs: P.kwargs
) -> Result[T, Exception]:
    try:
        return Ok(func(*args, **kwargs))
    except Exception as e:
        return Error(e)


def as_result(
    func: Callable[P, T], exceptions: tuple[type[_AnyException], ...] = (Exception,)
) -> Callable[P, Result[T, _AnyException]]:
    @wraps(func)
    def _wrapped(*args: P.args, **kwargs: P.kwargs) -> Result[T, _AnyException]:
        try:
            return Ok(func(*args, **kwargs))
        except exceptions as e:
            return Error(e)

    return _wrapped


class Ok(Generic[T, E]):
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


class Error(Generic[T, E]):
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
