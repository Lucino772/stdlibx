from stdlibx.result.fn.base import (
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
from stdlibx.result.fn.collect import collect, collect_all

__all__ = [
    "and_",
    "and_then",
    "collect",
    "collect_all",
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
    from stdlibx.result.fn.option import err, ok, transpose

    __all__ += ["err", "ok", "transpose"]
except ImportError:
    pass
