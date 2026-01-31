from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Mapping,
    Protocol,
    TypeVar,
    runtime_checkable,
)

if TYPE_CHECKING:
    from stdlibx.config._types import Loader

T = TypeVar("T", covariant=True)


@runtime_checkable
class _PydanticValidator(Protocol[T]):
    def model_validate(self, obj: Any, *, from_attributes: bool) -> T: ...


def load_config(
    validator: _PydanticValidator[T] | Callable[[Mapping[str, Any]], T],
    loaders: list[Loader],
) -> T:
    _ret = {key: val for loader in loaders for key, val in loader.load().items()}
    if isinstance(validator, _PydanticValidator):
        return validator.model_validate(_ret, from_attributes=False)
    return validator(_ret)
