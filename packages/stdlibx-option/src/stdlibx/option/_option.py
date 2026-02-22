from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, Callable, Generic, TypeVar

from stdlibx.option.types import Nothing, Some
from typing_extensions import ParamSpec, TypeIs

if TYPE_CHECKING:
    from stdlibx.option.types import Operation, Option


T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
P = ParamSpec("P")


def some(value: T) -> Option[T]:
    return _Some(value)


def nothing() -> Option[T]:
    return _Nothing()


def is_some(opt: Option[T]) -> TypeIs[Some[T]]:
    return opt.is_some()


def is_none(opt: Option[T]) -> TypeIs[Nothing]:
    return opt.is_none()


def maybe(func: Callable[P, T | None], *args: P.args, **kwargs: P.kwargs) -> Option[T]:
    value = func(*args, **kwargs)
    if value is None:
        return nothing()
    return some(value)


def optional(func: Callable[P, T | None]) -> Callable[P, Option[T]]:
    @wraps(func)
    def _wrapped(*args: P.args, **kwargs: P.kwargs) -> Option[T]:
        result = func(*args, **kwargs)
        if result is None:
            return nothing()
        return some(result)

    return _wrapped


class _Some(Generic[T]):
    __match_args__ = ("value",)
    __slots__ = ("value",)

    value: T

    def __init__(self, value: T) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Some({self.value!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Some):
            return other.value == self.value
        return False

    def is_some(self):
        return True

    def is_none(self):
        return False

    def apply(self, operation: Operation[Option[T], U]) -> U:
        return operation(self)


class _Nothing:
    __slots__ = ()

    def __repr__(self) -> str:
        return "Nothing()"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Nothing)

    def is_some(self):
        return False

    def is_none(self):
        return True

    def apply(self, operation: Operation[Option[T], U]) -> U:
        return operation(self)
