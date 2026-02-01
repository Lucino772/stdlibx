from __future__ import annotations


class OptionError(Exception): ...


class OptionUnwrapError(OptionError): ...


class OptionExpectError(OptionError): ...
