from stdlibx.result.methods.base import (
    and_,
    and_then,
    expect,
    expect_err,
    flatten,
    inspect,
    inspect_err,
    is_err_and,
    is_ok_and,
    map_,
    map_err,
    map_or,
    map_or_else,
    or_,
    or_else,
    unwrap,
    unwrap_err,
    unwrap_or,
    unwrap_or_else,
    unwrap_or_raise,
    zipped,
)

__all__ = [
    "and_",
    "and_then",
    "expect",
    "expect_err",
    "flatten",
    "inspect",
    "inspect_err",
    "is_err_and",
    "is_ok_and",
    "map_",
    "map_err",
    "map_or",
    "map_or_else",
    "or_",
    "or_else",
    "unwrap",
    "unwrap_err",
    "unwrap_or",
    "unwrap_or_else",
    "unwrap_or_raise",
    "zipped",
]

try:
    from stdlibx.result.methods.option import get_error, get_ok, transpose

    __all__ += ["get_error", "get_ok", "transpose"]
except ImportError:
    pass
