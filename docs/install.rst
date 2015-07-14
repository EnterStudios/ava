Installation guide
==================

.. _install:

AVA Install Instructions using Docker
-------------------------------------

AVA is designed to be built and run as a Docker container.

For those not familiar with Docker, it is an open-source project that
automates the deployment of applications inside software containers -
[Wikipedia](http://en.wikipedia.org/wiki/Docker_%28software%29)

Install Docker and Compose
--------------------------

* Docker installation instructions can be found here: [https://docs.docker.com/installation]
* Docker now has an orchestration layer called compose. 
* Installation instructions for compose can be found: [http://docs.docker.com/compose/install/]

Install and run AVA
-------------------

1. Pull down the latest version of the project ``git clone git@github.com:SafeStack/ava.git``
2. ``cd ava``
3. Use docker-compose to build the AVA application images and its dependencies and boot the app ``docker-compose up``
4. Browse to http://localhost:8000 to access the AVA web frontend.

