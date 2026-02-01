from stdlibx.option.methods.base import (
    and_,
    and_then,
    expect,
    filter_,
    flatten,
    inspect,
    is_none_or,
    is_some_and,
    map_,
    map_or,
    map_or_else,
    or_,
    or_else,
    unwrap,
    unwrap_or,
    unwrap_or_else,
    xor,
    zipped,
)

__all__ = [
    "and_",
    "and_then",
    "expect",
    "filter_",
    "flatten",
    "inspect",
    "is_none_or",
    "is_some_and",
    "map_",
    "map_or",
    "map_or_else",
    "or_",
    "or_else",
    "unwrap",
    "unwrap_or",
    "unwrap_or_else",
    "xor",
    "zipped",
]

try:
    from stdlibx.option.methods.result import ok_or, ok_or_else, transpose

    __all__ += ["ok_or", "ok_or_else", "transpose"]
except ImportError:
    pass
