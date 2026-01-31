from __future__ import annotations


class CancellationTokenError(Exception):
    """Base class for all cancellation-related errors. Raised when a
    cancellation event affects the current operation. Serves as the common
    superclass for all token error types.
    """


class CancellationTokenCancelledError(CancellationTokenError):
    """Raised when an operation is cancelled via a cancellation token. This
    exception indicates that the token was explicitly cancelled.
    """


class CancellationTokenTimeoutError(CancellationTokenError):
    """Raised when a token is cancelled due to a timeout. This exception
    indicates that the token's cancellation was triggered by an internal
    timeout mechanism (for example via :func:`stdlibx.cancel.with_timeout`).
    """
