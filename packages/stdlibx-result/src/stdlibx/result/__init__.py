from stdlibx.result._collect import collect, collect_all
from stdlibx.result._errors import ResultError, ResultExpectError, ResultUnwrapError
from stdlibx.result._operations.base import (
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
from stdlibx.result._result import error, is_err, is_ok, ok, safe, try_

__all__ = [
    "ResultError",
    "ResultExpectError",
    "ResultUnwrapError",
    "and_",
    "and_then",
    "collect",
    "collect_all",
    "error",
    "expect",
    "expect_err",
    "flatten",
    "inspect",
    "inspect_err",
    "is_err",
    "is_err_and",
    "is_ok",
    "is_ok_and",
    "map_",
    "map_err",
    "map_or",
    "map_or_else",
    "ok",
    "or_",
    "or_else",
    "safe",
    "try_",
    "unwrap",
    "unwrap_err",
    "unwrap_or",
    "unwrap_or_else",
    "unwrap_or_raise",
    "zipped",
]

try:
    from stdlibx.result._operations.option import get_error, get_ok, transpose

    __all__ += ["get_error", "get_ok", "transpose"]
except ImportError:
    pass
