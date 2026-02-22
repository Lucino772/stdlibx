from stdlibx.option._collect import collect, collect_all
from stdlibx.option._errors import OptionError, OptionExpectError, OptionUnwrapError
from stdlibx.option._operations.base import (
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
from stdlibx.option._option import (
    as_optional,
    is_none,
    is_some,
    nothing,
    optional_of,
    some,
)

__all__ = [
    "OptionError",
    "OptionExpectError",
    "OptionUnwrapError",
    "and_",
    "and_then",
    "as_optional",
    "collect",
    "collect_all",
    "expect",
    "filter_",
    "flatten",
    "inspect",
    "is_none",
    "is_none_or",
    "is_some",
    "is_some_and",
    "map_",
    "map_or",
    "map_or_else",
    "nothing",
    "optional_of",
    "or_",
    "or_else",
    "some",
    "unwrap",
    "unwrap_or",
    "unwrap_or_else",
    "xor",
    "zipped",
]

try:
    from stdlibx.option._operations.result import ok_or, ok_or_else, transpose

    __all__ += ["ok_or", "ok_or_else", "transpose"]
except ImportError:
    pass
