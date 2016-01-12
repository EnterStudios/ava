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

* Docker installation instructions can be found `here <https://docs.docker.com/installation>`_.
* Docker now has an orchestration layer called compose. 
* Installation instructions for compose can be found `here <http://docs.docker.com/compose/install/>`_.

.. note::

   For Mac OS X developers, you will need to use `boot2docker <http://boot2docker.io/>`_ and `brew <http://brew.sh/>`_.

   If you get stuck with installation and setup we can help - :doc:`get_help`

Install and run AVA
-------------------

1. Pull down the latest version of the project ``git clone git@github.com:SafeStack/ava.git``
2. Change into the folder "ava" that you have cloned ``cd ava``
3. Make a copy of the file "secrets.env.example" and rename this copy as "secrets.env"
4. Store your secret key in the secrets.env file (If you don't know how to generate a secret key, go check out the django docs)
5. Build the docker images and do the initial configuration using ``docker-compose build``
5. Use docker-compose to boot the app ``docker-compose up`` (note this process may take some time)
6. Once you see the message ``Starting development server at http://0.0.0.0:8000/`` displayed on the console, browse to http://localhost:8000 to access the AVA web frontend.

.. note::

   If an error message occurs when trying to use ``docker-compose up`` that is to do with the docker daemon not being up and running , check what docker processes are running: ``ps aux | grep docker`` (for linux users).
   
   If there is no docker daemon process running you will need to start one manually: ``docker run`` (or ``boot2docker up`` on Mac OSX)
   
   Once this daemon is running you will need to restart you computer, navigate back into the "ava" folder and try ``docker-compose up`` again.


