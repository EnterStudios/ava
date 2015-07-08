import os
import enum

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
    # AVA Redirection Middleware must happen after AuthenticationMiddleware
    'ava.middleware.AVARedirectionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
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
    'debug_toolbar',
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

class REDIS_DATABASES(enum.IntEnum):

    """Define slots for our redis databases."""
    DJANGO_CACHING_FRAMEWORK = 0
    DJANGO_SESSION_FRAMEWORK = 1
    CELERY_BROKER = 2
    CELERY_RESULT_BACKEND = 3

USE_REDIS_SESSIONS = True  # Turned off for the moment -- not needed.
if USE_REDIS_SESSIONS:
    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', 'localhost')
    SESSION_REDIS_PORT = os.environ.get('REDIS_PORT_6379_TCP_PORT', '6379')
    SESSION_REDIS_DB = int(REDIS_DATABASES.DJANGO_SESSION_FRAMEWORK)
    SESSION_REDIS_PREFIX = 'session'

## Using redis for the cache would be nice, but the library is still buggy
## with Python 3, When they fix the bugs hopefully we can just flip this
## switch.
USE_REDIS_CACHE = False  # Disabled because of Python 3 compatibility bugs.
if USE_REDIS_CACHE:
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': (
                '{}:{}'.format(
                    os.environ.get('REDIS_PORT_6379_TCP_ADDR', 'localhost'),
                    os.environ.get('REDIS_PORT_6379_TCP_PORT', '6379'),
                )
            ),
            'OPTIONS': {
                'DB': REDIS_DATABASES.DJANGO_CACHING_FRAMEWORK,
            }
        },
    }

LOGIN_REDIRECT_URL = "/"

PUBLIC_SITE_URLS = [
    'http://localhost:8000/',
]

# IMPORT EMAIL SETTINGS
try:
    from .email import *  # noqa
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
BROKER_URL = 'redis://{}:{}/{}'.format(
    os.environ.get('REDIS_PORT_6379_TCP_ADDR', None),
    os.environ.get('REDIS_PORT_6379_TCP_PORT', None),
    REDIS_DATABASES.CELERY_BROKER
)
BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': 60 * 60,
    'fanout_prefix': True,
    'fanout_patterns': True,
}
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://{}:{}/{}'.format(
    os.environ.get('REDIS_PORT_6379_TCP_ADDR', None),
    os.environ.get('REDIS_PORT_6379_TCP_PORT', None),
    REDIS_DATABASES.CELERY_RESULT_BACKEND
)


## CONTENT SECURITY POLICY (CSP) CONFIGURATION
##
## Here is where we configure exemptions from the default (strong)
## CSP policy. In an ideal world, this will be empty.
##
## Documented at: http://django-csp.readthedocs.org/en/latest/configuration.html
##
## CSP crash course at: http://django-csp.readthedocs.org/en/latest/configuration.html

CSP_STYLE_SRC = (
    ## 'self' is for all local assets, the usual default.
    "'self'",

    ## Unfortunately 'modernizr' seems to require 'unsafe-inline' styles.
    "'unsafe-inline'",

    ## CDN for a stylesheet we're pulling in.
    "http://maxcdn.bootstrapcdn.com/"
)

CSP_SCRIPT_SRC = (
    "'self'",
    ## lodash.min.js requires the use of 'unsafe-eval', which is a shame.
    "'unsafe-eval'",

    ## JQuery is being pulled from a CDN.
    "http://ajax.googleapis.com",

    ## This sha256 excemption is for the tiny little bit of javascript
    ## that the django-html5-boilerplate library is injecting at the
    ## bottom of seemingly every page. It would be nice for this to go
    ## away somehow.
    "'sha256-QElWz9ZyO3cMaja_DMF2vK4SfsTklXYMigNFQGuxka8='",
)

CSP_FONT_SRC = (
    "'self'",
    ## Bootstrap CDN
    "http://maxcdn.bootstrapcdn.com/",
)

CSP_IMG_SRC = (
    "'self'",

    ## This might not be necessary. Not having it in place was
    ## Causing a CSP violation because of an image Lastpass
    ## injects into form fields. If that's actually the only
    ## reason we're seeing those violations, than later we can
    ## remove this exemption again.
    "data:",
)


## GOOGLE OAUTH2 CONFIGURATION
GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID', None)
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET', None)


# DJANGO DEBUG TOOLBAR CONFIGURATION
def _show_toolbar_callback(request):
    return DEBUG
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': _show_toolbar_callback,
}
