stdlibx-cancel
==============

.. toctree::
   :maxdepth: 1
   :hidden:

   Getting Started <self>
   Reference <reference/stdlibx.cancel>

This package provides simple support for cancelling long-running operations in a controlled and predictable way. It lets you create cancellation tokens, cancel them manually or with a timeout, check their state, and register callbacks to run when cancellation occurs.

Installation
------------


.. tab:: pip

    .. code-block:: bash

        pip install stdlibx-cancel

.. tab:: uv

    .. code-block:: bash

        uv add stdlibx-cancel

.. tab:: poetry

    .. code-block:: bash

        poetry add stdlibx-cancel

.. tab:: pipenv

    .. code-block:: bash

        pipenv install stdlibx-cancel

Examples
--------

Basic Cancellation
~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :emphasize-lines: 13,20,28

    import time
    from threading import Thread

    from stdlibx.cancel import (
        CancellationToken,
        default_token,
        is_token_cancelled,
        with_cancel,
    )

    def long_running_task(cancel_token: CancellationToken):
        for i in range(1000):
            if is_token_cancelled(cancel_token):
                print("Task cancelled!")
                break

            print(f"Processing item {i}")

    # Create a cancellation token
    token, cancel = with_cancel(default_token())

    # Start long-running task
    th = Thread(target=long_running_task, args=(token,))
    th.start()

    # Cancel token and wait for thread to join
    time.sleep(5)
    cancel()
    th.join()


Timeout Cancellation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :emphasize-lines: 12,19

    from threading import Thread

    from stdlibx.cancel import (
        CancellationToken,
        default_token,
        is_token_cancelled,
        with_timeout,
    )

    def long_running_task(cancel_token: CancellationToken):
        for i in range(1000):
            if is_token_cancelled(cancel_token):
                print("Task cancelled!")
                break

            print(f"Processing item {i}")

    # Create a cancellation token, token is cancelled automatically after 5 seconds
    token, cancel = with_timeout(default_token(), 5)

    # Start long-running task
    th = Thread(target=long_running_task, args=(token,))
    th.start()

    # Wait for thread to join
    th.join()

Callbacks
~~~~~~~~~

.. code-block:: python
    :emphasize-lines: 12,22,23

    from threading import Thread

    from stdlibx.cancel import (
        CancellationToken,
        default_token,
        is_token_cancelled,
        with_timeout,
    )

    def long_running_task(cancel_token: CancellationToken):
        for i in range(1000):
            if is_token_cancelled(cancel_token):
                print("Task cancelled!")
                break

            print(f"Processing item {i}")

    def run_on_cancel(*args):
        print("Token was cancelled (callback)")

    # Create a cancellation token, token is cancelled automatically after 5 seconds
    token, cancel = with_timeout(default_token(), 5)
    token.register(run_on_cancel)

    # Start long-running task
    th = Thread(target=long_running_task, args=(token,))
    th.start()

    # Wait for thread to join
    th.join()
