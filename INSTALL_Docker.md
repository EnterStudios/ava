## AVA Install Instructions using Docker

> This guide is a work in progress, help us by submitting pull requests with bits we missed.

For those not familiar with Docker, it is an open-source project that automates the deployment of applications inside software containers - [Wikipedia](http://en.wikipedia.org/wiki/Docker_%28software%29)

---

### Install Docker and Compose

* Docker installation instructions can be found here: [https://docs.docker.com/installation]
* Docker now has an orchestration layer called compose. 
* Installation instructions for compose can be found: [http://docs.docker.com/compose/install/]

---

### Install AVA

1. Pull down the latest version of the project `git clone git@github.com:SafeStack/ava.git`
2. `cd ava`
3. Get Compose to build the AVA image including the dependancies and requirements `docker-compose build`
4. Create file for your local settings from template `cp local_settings.py.example local_settings.py`
5. Using your prefered editor, edit `local_settings.py` changing the database and redis server settings. See below for further details.
6. Create migrations for the database schema with `docker-compose run --rm web python src/manage.py makemigrations`
7. Run migrations to create tables `docker-compose run --rm web python src/manage.py migrate`
8. Create our first user `docker-compose run --rm web python src/manage.py createsuperuser`
9. Run AVA! `docker-compose up -d`
10. To view AVA in a browser, identify the IP of your docker instance `docker ip` and visit `http://<ip address>:8000` in your web browser.

### Local_Settings.py changes

The Docker configuration we are now using to run AVA is made up of three different containers, AVA itself (derived from a container image with Python preinstalled), a Redis container and a PostgreSQL container. Because all these containers are separate, AVA is no longer talking to a Redis instance via Unix sockets and is also no longer talking to PostgreSQL on localhost. Fortunately Docker takes care of the networking and host name resolution for us, but we need to configure the local_settings.py to use network connectivity using the names specified in the fig.yml file, for example:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'changeme',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```  
and for Redis  
```python
# Redis socket location
#SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'
# Or use TCP
SESSION_REDIS_HOST = 'redis'
SESSION_REDIS_PORT = 6379
```
