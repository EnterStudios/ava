## AVA Install Instructions

> This guide is a work in progress, help us by submitting pull requests with bits we missed.

AVA is a Django application and requires Python 2.7, Redis and PostreSQL.

We're not production ready yet so these instructions are for setting up your development environment.

* [Setup Fedora 21](https://github.com/ladynerd/ava/blob/master/INSTALL.md#fedora-setup)
* [Setup Ubuntu 14.04](https://github.com/ladynerd/ava/blob/master/INSTALL.md#ubuntu-setup)
* [Install AVA](https://github.com/ladynerd/ava/blob/master/INSTALL.md#install-ava)

---

### Fedora Setup

The following assumes a basic Fedora 21 Server has been setup with no requisite packages.

Install the packages that we will need:
```
sudo yum update -y
sudo yum groupinstall "Development Tools"
sudo yum install postgresql-server postgresql-contrib postgresql redis python-pip python-devel libpqxx libpqxx-devel openldap-devel
```

##### PostgreSQL
```
sudo postgresql-setup initdb  
sudo sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /var/lib/pgsql/data/postgresql.conf  
echo "host    all    all    0.0.0.0/0    md5" | sudo tee -a /var/lib/pgsql/data/pg_hba.conf  
```

If using localhost for the database connection, you'll need to add following above existing localhost entry in pg_hba.conf  
```
host    avadata         all             127.0.0.1/32            md5
```

Then configure PostgreSQL to start automatically
```
sudo systemctl enable postgresql.service  
sudo systemctl start postgresql.service  
sudo systemctl status postgresql.service
```
Create the user and database
```
sudo -u postgres createuser --pwprompt avasecure  
sudo -u postgres createdb --owner "avasecure" avadata  
```

##### Redis
```
sudo systemctl enable redis.service  
sudo systemctl start redis.service  
```

Edit `/etc/redis.conf` and uncomment/change the following lines:
```
unixsocket /var/run/redis/redis.sock
unixsocketperm 700
```
Restart the redis server for settings to take effect, 
`sudo service redis-server restart`

```
sudo systemctl restart redis.service  
```

---

### Ubuntu Instructions

The following are instructions to build on a basic Ubuntu server build

Install the packages that we will need:
``` 
sudo apt-get build-essential git python-pip python-dev libpqxx-4.0 libpqxx-dev libldap2-dev libsasl2-dev libssl-dev redis-server postgresql postgresql-contrib postgresql-client -y
```

##### Install PostgreSQL
```
sudo sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /etc/postgresql/9.3/main/postgresql.conf  
echo "host    all    all    0.0.0.0/0    md5" | sudo tee -a /etc/postgresql/9.3/main/pg_hba.nf  
sudo service postgresql restart
```

Next create the user and database  
```
sudo -u postgres createuser --pwprompt avasecure  
sudo -u postgres createdb --owner "avasecure" avadata  
```

##### Install Redis

Edit `/etc/redis/redis.conf` and uncomment/change the following lines:
```
unixsocket /var/run/redis/redis.sock
unixsocketperm 755
```
Restart the redis server for settings to take effect, 
`sudo service redis-server restart`


__If you get a "ImportError: cannot import name IncompleteRead" then:__  
```
sudo apt-get remove python-pip
sudo easy_install pip
```

---

### Install AVA

1. Pull down the latest version of the project `git clone git@github.com:ladynerd/ava.git`
2. `cd ava`
3. Install the required python packages with `pip install -r config/requirements.txt` if not using something like virtualenv you might need to use `sudo`
4. Create file for your local settings from template `cp local_settings.py.example local_settings.py`
5. Using your prefered editor, edit `local_settings.py` changing the database and redis server settings.
6. Create migrations for the database schema with `python manage.py makemigrations`
7. Run migrations to create tables `python manage.py migrate`
8. Create our first user `python manage.py createsuperuser`
9. Run AVA! `python manage.py runserver` and visit http://localhost:8000 in your browser.
