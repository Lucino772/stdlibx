from __future__ import annotations


class ResultError(Exception): ...


class ResultUnwrapError(ResultError): ...


class ResultExpectError(ResultError): ...
