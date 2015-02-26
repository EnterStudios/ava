## AVA Install Instructions using Docker

> This guide is a work in progress, help us by submitting pull requests with bits we missed.

For those not familiar with Docker, it is an open-source project that automates the deployment of applications inside software containers - [Wikipedia](http://en.wikipedia.org/wiki/Docker_%28software%29)

If you have read the previous install instructions you will realise there are several dependancies and an amount of configuration required to run AVA. By using Docker most of this is taken care of and what you are left with is the steps below. However first we must ensure Docker is available. This means installing both Docker and another utility called Fig onto the machine you wish to run AVA on. I should point out Docker is not a virtualisation system such as VMware/Virtualbox, you can happily run Docker containers inside a VM.

At this time it appears that Docker is far easier to install on Fedora than Ubuntu as you will see. Also note the utility Fig is in the process of being incorporated into the base Docker eco-system and in future will be known as docker-compose, but for now the current version will be fine for our purposes.


* [Setup Fedora 21](https://github.com/ladynerd/ava/blob/master/INSTALL_Docker.md#fedora-setup)
* [Setup Ubuntu 14.04](https://github.com/ladynerd/ava/blob/master/INSTALL_Docker.md#ubuntu-setup)

---

### Fedora Setup

The following assumes a basic Fedora 21 Server has been setup with no requisite packages.

Install the packages that we will need to install AVA with Docker:
```sh
sudo yum update -y  
sudo yum install git fig docker  
```

##### Install AVA

1. Pull down the latest version of the project `git clone git@github.com:ladynerd/ava.git`
2. `cd ava`
3. Get Fig to build the AVA image including the dependancies and requirements `sudo fig build`
4. Create file for your local settings from template `cp local_settings.py.example local_settings.py`
5. Using your prefered editor, edit `local_settings.py` changing the database and redis server settings. See below for further details.
6. Create migrations for the database schema with `sudo fig run --rm web python manage.py makemigrations`
7. Run migrations to create tables `sudo fig run --rm web python manage.py migrate`
8. Create our first user `sudo fig run --rm web python manage.py createsuperuser`
9. Run AVA! `sudo fig up -d` and visit http://localhost:8000 in your browser.

Some useful fig commands are are listed below including their uses.


---

### Ubuntu Instructions

The following are instructions to build on a basic Ubuntu server build

Install the packages that we will need:
``` 
sudo apt-get build-essential git python-pip python-dev libpqxx-4.0 libpqxx-dev libldap2-dev libsasl2-dev libssl-dev redis-server postgresql postgresql-contrib postgresql-client -y
```

##### Install AVA

---

### Useful Fig commands
* To see what containers are running: `sudo fig ps`

* To view the output of running containers: `sudo fig logs`

* To stop all running container: `sudo fig stop`

* To start containers in the foreground: `sudo fig up`

* To remove stopped containers from your system: `sudo fig rm`



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
