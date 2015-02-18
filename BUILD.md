## AVA Build instructions

The instructions allow you to build AVA on either Fedora 21 or Ubuntu 14.04 LTS.

AVA is a Django application and requires Python 2.7, Redis and PostreSQL.

---

### Fedora Instructions

The following assumes a basic Fedora 21 Server has been setup with no requisite packages.

First update Fedora and install the developer tools:  
```
sudo yum update -y  
sudo yum groupinstall "Development Tools" -y
```

#### Install PostgreSQL
```
sudo yum install postgresql-server postgresql-contrib postgresql -y  
sudo postgresql-setup initdb  
sudo sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /var/lib/pgsql/data/postgresql.conf  
echo "host    all    all    0.0.0.0/0    md5" | sudo tee -a /var/lib/pgsql/data/pg_hba.conf  
```

If using localhost for the database connection, you'll need to add following above existing localhost entry in pg_hba.conf  
```
host    avadata         all             127.0.0.1/32            md5
```

Then configure PostgreSQL to start automatically and create the user and database  
```
sudo systemctl enable postgresql.service  
sudo systemctl start postgresql.service  
sudo systemctl status postgresql.service
```

```
sudo -u postgres createuser --pwprompt avasecure  
sudo -u postgres createdb --owner "avasecure" avadata  
```

#### Install Redis
```
sudo yum install redis -y  
sudo systemctl enable redis.service  
sudo systemctl start redis.service  
sudo nano /etc/redis.conf  
```

Uncomment/Change the following lines:  
__unixsocket /var/run/redis/redis.sock__  
__unixsocketperm 700__  

```
sudo systemctl restart redis.service  
```

#### Install Django and requisites
```
sudo yum install python-pip django python-devel libpqxx libpqxx-devel openldap-devel -y  
```

#### Configure AVA
```
sudo firewall-cmd --zone=FedoraServer --add-port=8000/tcp  
sudo mkdir -p /opt/ava  
sudo git clone https://github.com/ladynerd/ava.git /opt/ava  
cd /opt/ava/  
sudo pip install -r config/requirements.txt  
sudo pip install Whoosh  
sudo cp example_local_settings.py local_settings.py  
sudo nano local_settings.py  
sudo python manage.py makemigrations  
sudo python manage.py migrate  
sudo python manage.py createsuperuser  
sudo python manage.py runserver 0.0.0.0:8000  
```

Example local_settings.py changes:  
```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.  
        'NAME': 'avadata',                      # Or path to database file if using sqlite3.  
        'USER': 'avasecure',                      # Not used with sqlite3.  
        'PASSWORD': '<my frikin awesome password>',                  # Not used with sqlite3.  
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.  
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.  
    }  
}
```

---

### Ubuntu Instructions

The following are instructions to build on a basic Ubuntu server build

Like Fedora, first lets update  
``` 
sudo apt-get dist-upgrade -y  
sudo apt-get build-essential git -y  
```

#### Install PostgreSQL
```
sudo apt-get install postgresql postgresql-contrib postgresql-client -y  
sudo sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /etc/postgresql/9.3/main/postgresql.conf  
echo "host    all    all    0.0.0.0/0    md5" | sudo tee -a /etc/postgresql/9.3/main/pg_hba.conf  
sudo service postgresql restart  
```

Next create the user and database  
```
sudo -u postgres createuser --pwprompt avasecure  
sudo -u postgres createdb --owner "avasecure" avadata  
```

#### Install Redis
```
sudo apt-get install redis-server -y  
sudo nano /etc/redis/redis.conf  
```
Uncomment/Change the following lines:  
__unixsocket /var/run/redis/redis.sock__  
__unixsocketperm 755__  

```
sudo service redis-server restart  
```

#### Install Django and requisites
```
sudo apt-get install python-pip python-django python-dev libpqxx-4.0 libpqxx-dev libldap2-dev libsasl2-dev libssl-dev -y  
```

__If you get a "ImportError: cannot import name IncompleteRead" then:__  
```
sudo apt-get remove python-pip  
sudo easy_install pip  
```

#### Configure AVA
```
sudo mkdir -p /opt/ava  
sudo pip install -r config/requirements.txt  
sudo pip install Whoosh  
sudo cp example_local_settings.py local_settings.py  
sudo nano local_settings.py  
sudo python manage.py makemigrations  
sudo python manage.py migrate  
sudo python manage.py createsuperuser  
sudo python manage.py runserver 0.0.0.0:8000  
```

See above for example local_settings changes.
