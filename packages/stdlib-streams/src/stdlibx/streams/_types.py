from __future__ import annotations

from typing import Callable, Protocol, TypeVar, runtime_checkable

from typing_extensions import TypeAlias

T = TypeVar("T")
U = TypeVar("U")

Operation: TypeAlias = Callable[[T], U]


T_co = TypeVar("T_co", covariant=True)
U_contra = TypeVar("U_contra", contravariant=True)


class Disposable(Protocol):
    def dispose(self) -> None: ...


@runtime_checkable
class Observable(Protocol[T_co]):
    def apply(self, func: Operation[Observable[T_co], U_contra]) -> U_contra: ...

    def __or__(self, func: Operation[Observable[T_co], U_contra]) -> U_contra: ...

    def subscribe(self, func: Callable[[T_co], None]) -> Disposable: ...


class Observer(Protocol[U_contra]):
    def push(self, val: U_contra) -> None: ...


Subscriber: TypeAlias = Callable[[Observer[T]], Disposable]
