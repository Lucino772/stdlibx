from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, Callable, Generic, TypeVar

from typing_extensions import ParamSpec, TypeAlias, TypeGuard

if TYPE_CHECKING:
    from stdlibx.option._types import Operation


T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")
P = ParamSpec("P")

Option: TypeAlias = "Some[T] | Nothing[T]"


def is_some(opt: Option[T]) -> TypeGuard[Some[T]]:
    return opt.is_some()


def is_none(opt: Option[T]) -> TypeGuard[Nothing[T]]:
    return opt.is_none()


def optional_of(
    func: Callable[P, T | None], *args: P.args, **kwargs: P.kwargs
) -> Option[T]:
    value = func(*args, **kwargs)
    if value is None:
        return Nothing()
    return Some(value)


def as_optional(func: Callable[P, T | None]) -> Callable[P, Option[T]]:
    @wraps(func)
    def _wrapped(*args: P.args, **kwargs: P.kwargs) -> Option[T]:
        result = func(*args, **kwargs)
        if result is None:
            return Nothing()
        return Some(result)

    return _wrapped


class Some(Generic[T]):
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


class Nothing(Generic[T]):
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
