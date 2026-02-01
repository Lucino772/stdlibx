from stdlibx.result._errors import ResultError, ResultExpectError, ResultUnwrapError
from stdlibx.result._result import (
    Error,
    Ok,
    Result,
    as_result,
    is_err,
    is_ok,
    result_of,
)

__all__ = [
    "Error",
    "Ok",
    "Result",
    "ResultError",
    "ResultExpectError",
    "ResultUnwrapError",
    "as_result",
    "is_err",
    "is_ok",
    "result_of",
]
