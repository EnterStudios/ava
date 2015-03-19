import os, sys


# ===========================
# = Directory Declaractions =
# ===========================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH 		= os.path.dirname(os.path.abspath(__file__))
CURRENT_DIR   		= os.path.dirname(__file__)
#TEMPLATE_DIRS 		= (os.path.join(CURRENT_DIR, 'templates'),)
STATICFILES_DIRS 	= (os.path.join(CURRENT_DIR, 'static'),)

DEBUG = True
TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
            os.path.join(BASE_DIR,  'ava/templates'),
            )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'media/'
MEDIA_URL = 'media/'
#STATIC_ROOT = 'static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'de)a(rpoh-cd&q#e0eq_!0fh_va&8j!9*q5$t0jb0stf#-@pt+'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'


DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


LOCAL_APPS = (
    'apps.ava_core',
    'apps.ava_core_group',
    'apps.ava_core_auth',
    'apps.ava_core_project',
    'apps.ava_core_ldap',
    'apps.ava_core_identity',
    'apps.ava_vis_graph',
    'apps.ava_test',
    'apps.ava_test_email',
    'apps.ava_test_twitter',
    'apps.ava_test_tracking',
)

THIRD_PARTY_APPS = (
    'dh5bp',
    'haystack',
    'ldap',
    'bootstrap3',
    'bootstrapform',
    'd3',
    'djrill',
    'twython',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

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

SHORTEN_MODELS = {
    'E': 'ava_test_email.EmailTest',
    'T': 'ava_test_twitter.TwitterTest',
}


SESSION_ENGINE = 'redis_sessions.session'

LOGIN_REDIRECT_URL= "/people/"

PUBLIC_SITE_URLS = [
    'http://localhost:8000/',
]


# IMPORT LOCAL SETTINGS

try:
    from local_settings import *
except ImportError:
    pass


# IMPORT EMAIL SETTINGS

try:
    from email_settings import *
except ImportError:
    pass
