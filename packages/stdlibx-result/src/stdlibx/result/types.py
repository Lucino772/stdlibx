from __future__ import annotations

from typing import Callable, Literal, Protocol, TypeVar, runtime_checkable

from typing_extensions import TypeAlias

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")

Operation: TypeAlias = Callable[[T], U]


@runtime_checkable
class Ok(Protocol[T]):
    __match_args__ = ("value",)
    value: T

    def is_ok(self) -> Literal[True]: ...
    def is_err(self) -> Literal[False]: ...
    def apply(self, operation: Operation[Result[T, E], U]) -> U: ...


@runtime_checkable
class Error(Protocol[E]):
    __match_args__ = ("error",)
    error: E

    def is_ok(self) -> Literal[False]: ...
    def is_err(self) -> Literal[True]: ...
    def apply(self, operation: Operation[Result[T, E], U]) -> U: ...


Result: TypeAlias = Ok[T] | Error[E]
