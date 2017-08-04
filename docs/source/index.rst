.. methodalyze documentation master file, created by
   sphinx-quickstart on Fri Aug  5 15:24:19 2016.
   Template rendered by cookiecutter on Fri Aug  4 11:21:01 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. only:: prerelease

    .. warning:: This is the documentation for a development version of methodalyze.

        .. only:: readthedocs

            `Documentation for the Most Recent Stable Version <http://methodalyze.readthedocs.io/en/stable>`_

Welcome to :code:`methodalyze`
==============================

Evaluate the reproducibility of scientific protocols.


.. =========== =============== ================== ======================= ====================
    Stable      |stable_build|  |stable_coverage|  |stable_documentation|  |stable_pyversions|
    Development |develop_build| |develop_coverage| |develop_documentation| |develop_pyversions|
    =========== =============== ================== ======================= ====================

    .. |stable_build| image:: https://travis-ci.org/scolby33/methodalyze.svg?branch=master
        :target: https://travis-ci.org/scolby33/methodalyze
        :alt: Stable Build Status
    .. |stable_coverage| image:: https://codecov.io/github/scolby33/methodalyze/coverage.svg?branch=master
        :target: https://codecov.io/github/scolby33/methodalyze?branch=master
        :alt: Stable Test Coverage Status
    .. |stable_documentation| image:: http://readthedocs.org/projects/methodalyze/badge/?version=stable
        :target: http://methodalyze.readthedocs.io/en/stable/?badge=stable
        :alt: Stable Documentation Status
    .. |stable_pyversions| image:: https://img.shields.io/badge/python-2.7%2C%203.5-blue.svg
        :alt: Stable Supported Python Versions

    .. |develop_build| image:: https://travis-ci.org/scolby33/methodalyze.svg?branch=develop
        :target: https://travis-ci.org/scolby33/methodalyze
        :alt: Development Build Status
    .. |develop_coverage| image:: https://codecov.io/github/scolby33/methodalyze/coverage.svg?branch=develop
        :target: https://codecov.io/github/scolby33/methodalyze?branch=develop
        :alt: Development Test Coverage Status
    .. |develop_documentation| image:: http://readthedocs.org/projects/methodalyze/badge/?version=develop
        :target: http://methodalyze.readthedocs.io/en/stable/?badge=develop
        :alt: Development Documentation Status
    .. |develop_pyversions| image:: https://img.shields.io/badge/python-2.7%2C%203.5-blue.svg
        :alt: Development Supported Python Versions

On this page:

.. contents::
    :local:


Installation
------------

.. toctree::
    :maxdepth: 2
    :hidden:

    installation

Installation should be as easy as executing this command in your chosen terminal::

    $ pip install methodalyze

The source code for this project is `hosted on Github <https://github.com/scolby33/methodalyze>`_.
Downloading and installing from source goes like this::

    $ git clone https://github.com/scolby33/methodalyze
    $ cd methodalyze
    $ pip install .

If you intend to install in a virtual environment, activate it before running :code:`pip install`.

See :ref:`installation` for further information about installing :code:`methodalyze` in all manner of ways.


Contributing
------------

.. toctree::
    :maxdepth: 2
    :hidden:

    contributing

:code:`methodalyze` is an open-source project, and, so far, is mostly a one-person effort.
Any contributions are welcome, be they bug reports, pull requests, or otherwise.
Issues are tracked on `Github <https://github.com/scolby33/methodalyze/issues>`_.

Check out :ref:`contributing` for more information on getting involved.


License Information
-------------------

.. toctree::
    :maxdepth: 2
    :hidden:

    license

:code:`methodalyze` is Copyright (c) 2017 Scott Colby. All rights reserved.

The full text of the license is available :ref:`here <license>` and in the root of the source code repository.


Changelog
---------

.. toctree::
    :maxdepth: 2
    :hidden:

    changelog

:code:`methodalyze` adheres to the Semantic Versioning ("Semver") 2.0.0 versioning standard.
Details about this versioning sheme can be found on the `Semver website <http://semver.org/spec/v2.0.0.html>`_
Versions postfixed with `-dev` are currently under development and those without a postfix are stable releases.

The current version of :code:`methodalyze` is |release|.

Full changelogs can be found on the :ref:`changelog` page.

.. toctree::
    :hidden:

    todo


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
