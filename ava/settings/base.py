import os, sys

## BASE_DIR is the path to the top level of the AVA project.
## That is: the root of the git repo, NOT the path to the
## AVA python package.
##
## The current layout is such that BASE_DIR is two directory
## levels up from the location of this settings file.
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '../..'
    )
)

DEBUG = True
TEMPLATE_DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_ENV_DB', 'postgres'),
        'USER': os.environ.get('DB_ENV_POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_ENV_POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('DB_PORT_5432_TCP_ADDR', ''),
        'PORT': os.environ.get('DB_PORT_5432_TCP_PORT', ''),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-nz'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

## TODO: Make configurable outside settings.
SECRET_KEY = 'de)a(rpoh-cd&q#e0eq_!0fh_va&8j!9*q5$t0jb0stf#-@pt+'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ava.urls'

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


LOCAL_APPS = (
    'ava.core',
    'ava.core_group',
    'ava.core_auth',
    'ava.core_project',
    'ava.import_ldap',
   # 'ava.import_google',
    'ava.core_identity',
    'ava.vis_graph',
    'ava.test',
    'ava.test_email',
    'ava.test_twitter',
    'ava.test_tracking',
)

THIRD_PARTY_APPS = (
    'dh5bp',
    'haystack',
    'ldap3',
    'bootstrap3',
    'bootstrapform',
    'd3',
    'djrill',
    'twython',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

## STATIC FILE CONFIGURATION
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


## REDIS CONFIGURATION
USE_REDIS_CACHE = False  # Turned off for the moment -- not needed.
if USE_REDIS_CACHE:
    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', None)
    SESSION_REDIS_PORT = os.environ.get('REDIS_PORT_6379_TCP_PORT', None)
    SESSION_REDIS_DB = 1
    SESSION_REDIS_PREFIX = 'session'

LOGIN_REDIRECT_URL= "/"

PUBLIC_SITE_URLS = [
    'http://localhost:8000/',
]

# IMPORT EMAIL SETTINGS
try:
    from .email import *
except ImportError:
    pass

## HAYSTACK CONFIGURATION
DOCKER_ELASTICSEARCH_URL = 'http://{}:{}'.format(
    os.environ.get('ELASTICSEARCH_PORT_9200_TCP_ADDR'),
    os.environ.get('ELASTICSEARCH_PORT_9200_TCP_PORT')
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': DOCKER_ELASTICSEARCH_URL,
        'INDEX_NAME': 'haystack',
    },
}


## (below commented out from local_settings.py)

## MANDRILL SETTINGS

#MANDRILL_API_KEY = "changeme"
#EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"


## CELERY CONFIGURATION

#BROKER_URL = 'amqp://avasecure:changeme@localhost:5672/avatasks'
#CELERY_ACCEPT_CONTENT = ['json']
#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'

