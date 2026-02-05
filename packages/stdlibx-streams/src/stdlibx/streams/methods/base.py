from __future__ import annotations

import operator
from functools import partial
from typing import (
    TYPE_CHECKING,
    Generic,
    TypeVar,
    Union,
)

from typing_extensions import TypeGuard, TypeVarTuple, Unpack

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

    from stdlibx.streams._types import (
        Disposable,
        Observable,
        Observer,
        Operation,
        Subscriber,
    )

T = TypeVar("T")
U = TypeVar("U")
Ts = TypeVarTuple("Ts")


def map_(source: Observable[T], func: Callable[[T], U]) -> Observable[U]:
    def _subscribe(other: Observer[U]) -> Disposable:
        return source.subscribe(lambda val: other.push(func(val)))

    return _Observable(_subscribe)


def if_(source: Observable[T], func: Callable[[T], bool]) -> Observable[T]:
    def _subscribe(other: Observer[T]) -> Disposable:
        return source.subscribe(
            lambda val: other.push(val) if func(val) is True else None
        )

    return _Observable(_subscribe)


def is_(
    source: Observable[Union[T, U]], func: Callable[[Union[T, U]], TypeGuard[U]]
) -> Observable[U]:
    def _subscribe(other: Observer[U]) -> Disposable:
        return source.subscribe(lambda val: other.push(val) if func(val) else None)

    return _Observable(_subscribe)


def is_not_none(source: Observable[Union[T, None]]) -> Observable[T]:
    return is_(source, lambda val: val is not None)  # type: ignore


def as_tuple(source: Observable[T]) -> Observable[tuple[T]]:
    return map_(source, lambda v: (v,))


def combine(
    source: Observable[tuple[Unpack[Ts]]], other: Observable[U]
) -> Observable[tuple[Unpack[Ts], U]]:
    values = {}

    def _update(observer: Observer[tuple[Unpack[Ts]]], **kwargs) -> None:
        nonlocal values
        values.update(kwargs)

        if ("first" not in values) or ("second" not in values):
            return

        if isinstance(values["first"], tuple):
            observer.push((*values["first"], values["second"]))  # type: ignore
        else:
            observer.push((values["first"], values["second"]))  # type: ignore

    def _subscribe(observer: Observer[tuple]) -> Disposable:
        _updater = partial(_update, observer)
        return _CompositeDisposable(
            [
                source.subscribe(lambda v: _updater(first=v)),
                other.subscribe(lambda v: _updater(second=v)),
            ]
        )

    return _Observable(_subscribe)


def start_with(source: Observable[T], value: T) -> Observable[T]:
    def _subscribe(other: Observer[T]) -> Disposable:
        other.push(value)
        return source.subscribe(other.push)

    return _Observable(_subscribe)


def for_(
    source: Observable[Iterable[T]], func: Callable[[T], U]
) -> Observable[Iterable[U]]:
    return map_(source, lambda items: [func(item) for item in items])


def distinct(
    source: Observable[T], equal_fn: Callable[[T, T], bool] = operator.eq
) -> Observable[T]:
    def _subscribe(other: Observer[T]) -> Disposable:
        curr_val: "Union[T, None]" = None

        def _subscriber(other: Observer[T], val: T) -> None:
            nonlocal curr_val
            if curr_val is None or equal_fn(curr_val, val) is False:
                other.push(val)
                curr_val = val

        return source.subscribe(partial(_subscriber, other))

    return _Observable(_subscribe)


class _Observable(Generic[T]):
    def __init__(self, subscribe: Subscriber[T]) -> None:
        self.__subscribe = subscribe

    def apply(self, func: Operation[Observable[T], U]) -> U:
        return func(self)

    def __or__(self, func: Operation[Observable[T], U]) -> U:
        return self.apply(func)

    def subscribe(self, func: Callable[[T], None]) -> Disposable:
        return self.__subscribe(_CallbackObserver(func))


class _CallbackObserver(Generic[T]):
    def __init__(self, func: Callable[[T], None]) -> None:
        self.__func = func

    def push(self, val: T) -> None:
        self.__func(val)


class _CompositeDisposable:
    def __init__(self, disposables: list[Disposable]) -> None:
        self.__disposables = disposables

    def dispose(self) -> None:
        for disposable in self.__disposables:
            disposable.dispose()
