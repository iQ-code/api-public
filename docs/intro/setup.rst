.. _setup:

===============
Getting started
===============

Inspiration-Q SDK is built as a Python library that can be installed and
consumed from your Python environment. The SDK is regularly tested on the
following platforms:

* **Linux:** 64-bit Ubuntu and Debian distributions
* **Windows:** 64-bit Windows 10

However, since it relies on standard Python tools, it should also work on any
other operating system with a modern Python 3 distribution.

Before installation
===================

It is recommended that the SDK be installed in a separate Python virtual
environment. A Python environment is a collection of libraries and a Python
interpreter that are configured as a unit. Environments can be activated and
modified separately from each other, adding new libraries, removing existing
ones or upgrading the Python interpreter. By working on a separate environment
you ensure that our SDK does not interact with unsupported software or obsolete
libraries.

The documentation assumes that you have installed a `Miniconda Python
distribution <https://docs.conda.io/en/latest/miniconda.html>`_, and that you
have also created and activated a Python environment with the name :code:`iQ` as
follows:

    .. code-block:: bash

        conda create -n iQ python numpy setuptools
        conda activate iQ

If you use other Python distributions, the steps for creating and activating the
environment may vary, and look something like

    .. code-block:: bash

        python -m venv iQ
        . iQ/bin/activate

Cloning the repository
======================

The recommended way to consume the library is to make a local copy of our SDK
from the official repository at https://github.com/inspirationq/api-public.
This may be done using a standard distribution of :code:`git`

    .. code-block:: bash

        git clone https://github.com/inspirationq/api-public.git

From within the newly created directory, the library may be installed using
Python's :code:`setuptools` as

    .. code-block:: bash

        python setup.py install

At any time, you may pull upgrades from the library using

    .. code-block:: bash

        git pull

If you do, make sure to reinstall the library, as explained above.


Using the SDK
=============

The :file:`examples` folder contains Jupyter notebooks that provide examples on
how to consume the library and put it to work on actual problems: somewhat
academic QUBO optimization problems, practical examples of the travelling
salesman problem, to portfolio optimization applications, etc.

The notebooks assume you have installed the library and have an internet connection
to access Inspiration-Q's API. At the beginning of each notebook there is a section
to insert the access token to the library, typically in AWS API Gateway format.
Other access options are discussed in the following sections.