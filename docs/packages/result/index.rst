stdlibx-result
==============

.. toctree::
   :maxdepth: 1
   :hidden:

   Getting Started <self>
   Reference <reference/stdlibx.result>

This package provides a result type that represents either a successful value (:py:class:`~stdlibx.result.Ok`) or an error (:py:class:`~stdlibx.result.Error`). Inspired by Rust's Result type, it enables explicit, functional error handling without relying on exceptions.

Installation
------------


.. tab:: pip

    .. code-block:: bash

        pip install stdlibx-result

.. tab:: uv

    .. code-block:: bash

        uv pip install stdlibx-result

.. tab:: poetry

    .. code-block:: bash

        poetry add stdlibx-result

.. tab:: pipenv

    .. code-block:: bash

        pipenv install stdlibx-result
