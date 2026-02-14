stdlibx-config
==============

.. toctree::
   :maxdepth: 1
   :hidden:

   Getting Started <self>
   Reference <reference/stdlibx.config>

This package provides utilities for loading and managing configuration from multiple sources, such as environment variables, JSON files, YAML files, and custom formats. It allows you to combine loaders and apply validation logic, making configuration flexible, composable, and easy to adapt to different environments.

Installation
------------


.. tab:: pip

    .. code-block:: bash

        pip install stdlibx-config

.. tab:: uv

    .. code-block:: bash

        uv add stdlibx-config

.. tab:: poetry

    .. code-block:: bash

        poetry add stdlibx-config

.. tab:: pipenv

    .. code-block:: bash

        pipenv install stdlibx-config

Example
-------

.. code-block:: python
    :emphasize-lines: 11-17

    from dataclasses import dataclass
    from typing import Any, Mapping

    from stdlibx.config import EnvLoader, JsonLoader, load_config

    @dataclass
    class Config: ...

    def validate_config(_: Mapping[str, Any]) -> Config: ...

    config = load_config(
        validate_config,
        [
            JsonLoader("path/to/config.json"),
            EnvLoader(),
        ],
    )
