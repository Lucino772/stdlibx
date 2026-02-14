Getting Started
===============

.. toctree::
   :maxdepth: 1
   :caption: Introduction
   :hidden:

   self
   genindex

.. toctree::
   :maxdepth: 1
   :caption: Packages
   :hidden:

   packages/cancel/index
   packages/compose/index
   packages/config/index
   packages/itertools/index
   packages/matchtools/index
   packages/option/index
   packages/result/index
   packages/streams/index


**stdlibx** is a collection of Python utilities that make common patterns easier to work with. You've probably dealt with a lot of None checks, exception handling that's hard to understand, and deeply nested conditionals. stdlibx helps you write cleaner code for these situations.

Philosophy
----------

- **Solve the actual problem:** Don't push any ideology. We just make code better.
- **Fit into Python:** Use what Python already offers. Nothing weird or foreign.
- **One thing per package:** Pick what you need. You're not locked in.
- **Keep it light:** Minimal dependencies means you stay in control.
- **Work together:** Use one package or combine them. Your choice.

Installation
------------

stdlibx packages are available on PyPI. Install individually or all at once:


.. tab:: pip

    .. code-block:: bash

        pip install stdlibx-result stdlibx-option stdlibx-compose

.. tab:: uv

    .. code-block:: bash

        uv add stdlibx-result stdlibx-option stdlibx-compose

.. tab:: poetry

    .. code-block:: bash

        poetry add stdlibx-result stdlibx-option stdlibx-compose

.. tab:: pipenv

    .. code-block:: bash

        pipenv install stdlibx-result stdlibx-option stdlibx-compose

Packages
--------

.. list-table::
   :widths: 20 40
   :header-rows: 1

   * - Package
     - What It Does
   * - :doc:`/packages/cancel/index`
     - Cancel long-running operations in a controlled way. Manage lifecycle, timeouts, and cleanup with explicit cancellation tokens.
   * - :doc:`/packages/compose/index`
     - Compose functions into clear, left-to-right pipelines. Build readable and reusable transformations.
   * - :doc:`/packages/config/index`
     - Load and combine configuration from multiple sources. Unify environment variables, files, and defaults in one place.
   * - :doc:`/packages/itertools/index`
     - Work with iterables in a functional style. Map, filter, reduce, and transform data without imperative loops.
   * - :doc:`/packages/matchtools/index`
     - Express branching logic declaratively. Replace nested if/elif chains with structured, ordered matching.
   * - :doc:`/packages/option/index`
     - Represent optional values explicitly. Avoid None checks by modeling presence and absence as a type.
   * - :doc:`/packages/result/index`
     - Model success and failure explicitly. Handle errors as values instead of relying on exceptions.
   * - :doc:`/packages/streams/index`
     - Build reactive and event-driven flows. Work with data that changes over time using composable streams.
