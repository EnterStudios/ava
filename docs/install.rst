Installation guide
==================

.. _install:

AVA Install Instructions using Docker
-------------------------------------

AVA is designed to be built and run as a Docker container.

For those not familiar with Docker, it is an open-source project that
automates the deployment of applications inside software containers - 
`Wikipedia <http://en.wikipedia.org/wiki/Docker_%28software%29>`_.

For more information on Docker go to the `Docker main site <https://www.docker.com/whatisdocker>`_.

Install Docker and Compose
--------------------------

* Docker installation instructions can be found here: `Linux <http://docs.docker.com/linux/started/>`_, `Windows <http://docs.docker.com/windows/started/>`_ and `Mac OS X <http://docs.docker.com/mac/started/>`_
* Docker now has an orchestration layer called compose. 
* Please note that at the moment compose (which will be necessary to run ava) is not currently supported by windows (and is mostly aimed at linux). 
* Installation instructions for compose can be found `here <http://docs.docker.com/compose/install/>`_.

.. note::

   For Mac OS X developers, you will need to use `boot2docker <http://boot2docker.io/>`_ and `brew <http://brew.sh/>`_.

   If you get stuck with installation and setup we can help - :doc:`get_help`

Install and run AVA
-------------------

1. Pull down the latest version of the project ``git clone git@github.com:SafeStack/ava.git``
2. ``cd ava``
3. Use docker-compose to build the AVA application images and its dependencies and boot the app ``docker-compose up``
4. Browse to http://localhost:8000 to access the AVA web frontend.


