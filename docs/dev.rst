===================
 Developer's Guide
===================

We are on the look out for testers, Django/Python developers,
documentation folk, graphics wizards, and UX people to help make AVA
awesome. If you have some spare cycles and want to contribute get
stuck in.

Bootstrapping a developer environment
=====================================

At this time, the Docker and Docker Compose configuration for AVA is
geared directly for development rather than production deployment. As
such, please refer to :ref:`install` for detailed instructions on
setting up your development environment.

Django project layout
=====================

AVA is laid out as a typical Django project::

    ava  (project root)
    ├── ava  (Python package)
    │   ├── abstract
            evaluate
            ...
    │   ├── settings (Django settings/conf files)
    │   ├── ...
    ├── bin  (utility scripts)
    │   └── in-container  (non-utility scripts)
    ├── docs  (project documentation)
    ├── requirements  (pip requirements)

Utility scripts
---------------

All utility scripts live in the ``bin/`` directory off the top
level. The scripts in ``bin/in-container/`` are not generally for
developer use -- they're called by other mechanisms from within
the context of a launched Docker container.

``./bin/auto-test.sh``
~~~~~~~~~~~~~~~~~~~~~~

This script launches a Docker container that uses ``inotify`` to
listen to file changes in the ``ava/`` Python package directory. Every
time a file is modified, it runs the Django test suite.

.. warning::

   At the moment, this script is only of use if Docker is running from
   Linux. It probably won't work in a ``boot2docker`` environment, but
   this hasn't yet been tested.

``./bin/flake8-checks.sh``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Runs the ``flake8`` static code analysis tool over the ava/ codebase
and reports on errors. This script is also executed as-is during the
test-suite run.

You can run this script as a quick check before a commit to see if the
test will pass.

.. note::

   If you run this script manually, it will expect the ``flake8`` tool
   to be installed locally on your machine. You can install it using
   ``pip install flake8``, or use ``./bin/test.sh`` to run the test
   suite in a Docker container.

``./bin/test.sh``
~~~~~~~~~~~~~~~~~

Launches a docker container to execute the AVA test suite. Any arguments
used are passed to the test runner.

``./bin/nuke-and-rebuild.sh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove and re-build the Docker images used in your development
environment. This script is just two commands right now, but it might
grow if we start loading standard data fixtures into our developer
environments.

After running this script and ``docker-compose up``, you should be back
to a basic running developer environment.

.. note::

   THIS SCRIPT WILL DELETE ALL DATA IN YOUR DATABASE. Remember you may need
   to recreate users after running this.

   The goal is that this script will always "just work". With a fresh
   repository and a working installation of Docker/docker-compose, if
   this script *doesn't* get you back to a working developer
   environment, then report it as a bug.

``./bin/database-flush.sh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove all the records from the database but leave the docker containers
intact. This is helpful if you are repeatedly testing data import and
need to flush out the records from one import before starting the next.

After running this script and ``docker-compose up``, you should be back
to a basic running developer environment.

``./bin/make-migrations.sh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A wrapper for Django's 'makemigrations' management command. Run this
after database model changes to (hopefully) autodetect and build the
correct migration files.

``./bin/create-superuser.sh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A wrapper for Django's 'createsuperuser' management command. Run this
after database model changes to create a superuser for AVA.

Python development guidelines
=============================

Logging
-------

Use the Python ``logging`` framework for all your
debug/informational/critical logging needs.

If the Python module you wish to add logging to doesn't already have
it, add the following::

  import logging
  log = logging.getLogger(__name__)

This will create a new logger which is named after the module it's in,
for example ``ava.welcome.views``. Once created, you can use the
logger as follows::

  log.debug('This is a simple debugging message')
  log.info('An informational message with %s interpolated in', my_variable)

The priority levels are ``debug``, ``info``, ``warning``, ``error``,
and ``critical``.

If you have caught an exception, a special syntax includes the
exception with the logging output::

  log.exception("Sorry, an error occurred", exc_info=e)

where '``e``' is the exception that was caught. This is *always* a good idea.

At present, all ``ava.*`` log messages are configured to be output to
the console.

Template development guidelines
===============================

Style development guidelines
============================

