stdlibx-compose
===============

.. toctree::
   :maxdepth: 1
   :hidden:

   Getting Started <self>
   Reference <reference/stdlibx.compose>

This package provides simple utilities for composing functions. It includes :py:meth:`~stdlibx.compose.flow` for applying functions left-to-right to a value, and :py:meth:`~stdlibx.compose.pipe` for building reusable function pipelines. This makes it easy to structure logic as small, composable steps.

Installation
------------


.. tab:: pip

    .. code-block:: bash

        pip install stdlibx-compose

.. tab:: uv

    .. code-block:: bash

        uv add stdlibx-compose

.. tab:: poetry

    .. code-block:: bash

        poetry add stdlibx-compose

.. tab:: pipenv

    .. code-block:: bash

        pipenv install stdlibx-compose

Examples
--------

Simple
~~~~~~

.. code-block:: python
    :emphasize-lines: 11-15

    from stdlibx.compose import flow, pipe

    # Define simple functions
    def double(x: int) -> int:
        return x * 2

    def add_ten(x: int) -> int:
        return x + 10

    # Compose left-to-right with flow
    result = flow(
        5,
        double,
        add_ten,
    )
    print(result)


Reusable Pipeline
~~~~~~~~~~~~~~~~~

.. code-block:: python
    :emphasize-lines: 6-10

    from typing import Callable

    from stdlibx.compose import pipe

    # Create a reusable pipeline
    process_numbers: Callable[[int], float] = pipe(
        lambda x: x * 2,
        lambda x: x + 5,
        lambda x: x / 2,
    )

    print(process_numbers(10))
    print(process_numbers(20))
