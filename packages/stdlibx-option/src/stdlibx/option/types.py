from __future__ import annotations

from typing import Callable, Literal, Protocol, TypeVar, Union, runtime_checkable

from typing_extensions import TypeAlias

T = TypeVar("T")
U = TypeVar("U")

Operation: TypeAlias = Callable[[T], U]


@runtime_checkable
class Some(Protocol[T]):
    __match_args__ = ("value",)

    value: T

    def is_some(self) -> Literal[True]: ...
    def is_none(self) -> Literal[False]: ...
    def apply(self, operation: Operation[Option[T], U]) -> U: ...


@runtime_checkable
class Nothing(Protocol):
    def is_some(self) -> Literal[False]: ...
    def is_none(self) -> Literal[True]: ...
    def apply(self, operation: Operation[Option[T], U]) -> U: ...


Option: TypeAlias = Union[Some[T], Nothing]
