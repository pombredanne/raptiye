# coding: utf-8
#
# raptiye
# Copyright (C) 2009  Alper Kanat <alperkanat@raptiye.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from datetime import date
import os
import sys

try:
    import django
except ImportError:
    sys.stderr.write("django couldn't be found.")
    sys.exit(1)

DOCUMENT_ROOT = os.path.abspath(os.path.dirname(__file__))
DJANGO_DIR = os.path.abspath(os.path.dirname(django.__file__))


# --- GENERIC SETTINGS ------------

PROJECT_NAME = u"raptiye"
PROJECT_SUBTITLE = u"Quis custodes ipsos custodiet?"

COLORIZE_CODE = False
ENABLE_EMOTIONS = True
ENTRIES_PER_PAGE = 3

RSS_LIMIT = 10
RSS_URL = ""

BIRTH_DATE = date(1984, 05, 16)


# --- ADMIN SETTINGS --------------

ADMIN_LIST_PER_PAGE = 100


# --- COMMENT SETTINGS ------------

DISQUS_SHORTNAME = PROJECT_NAME


# --- TAG SETTINGS ----------------

FORCE_LOWERCASE_TAGS = True
MAX_TAG_LENGTH = 50


# --- OTHER SETTINGS --------------

EMAIL_FAIL_SILENCE = True
EMAIL_HOST = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_HOST_USER = ""
EMAIL_INFO_ADDRESS_TR = ""
EMAIL_INFO_ADDRESS_EN = ""
# EMAIL_PORT =
EMAIL_SUBJECT_PREFIX = u""
EMAIL_USE_TLS = True
SERVER_EMAIL = ""

LOCALE = "tr_TR.UTF-8"

DEFAULT_CHARSET = 'utf-8'
DEFAULT_CONTENT_TYPE = 'text/html'
FILE_CHARSET = 'utf-8'

DATE_FORMAT = "d.m.Y"
DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y',
    '%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y',
    '%B %d, %Y', '%d %B %Y', '%d %B, %Y', '%d/%m/%Y',
    '%d.%m.%Y'
)

DATETIME_FORMAT = "H:i @ d.m.Y, l"
DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d',
    '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M', '%m/%d/%Y',
    '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M', '%m/%d/%y',
    '%d.%m.%Y', '%d/%m/%Y', '%d/%m/%Y %H:%M',
    '%d.%m.%Y %H:%M', '%d.%m.%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S',
)


# --- STANDARD DJANGO SETTINGS ----

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Alper Kanat', 'alperkanat@raptiye.org'),
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": '%s/raptiye.db' % DOCUMENT_ROOT
    }
}

TIME_ZONE = 'Europe/Istanbul'

LANGUAGE_CODE = 'tr'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''  # fill with absolute path
MEDIA_URL = '/static/upload/'
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    "%s/static" % DOCUMENT_ROOT,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'raptiye.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'raptiye.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'raptiye.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

TEMPLATE_DIRS = (
    "%s/templates/default" % DOCUMENT_ROOT,
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tagging',
    'raptiye.blog',
    'raptiye.contrib.flatpages'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] [%(asctime)s] [%(pathname)s] [%(lineno)d] %(message)s'
        },
    },
    'handlers': {
        'null': {
            'class': 'django.utils.log.NullHandler'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'rotate': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '%s/logs/raptiye.log' % DOCUMENT_ROOT,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        '': {  # default logger
            'handlers': ['console', 'rotate'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {  # handles 4xx & 5xx
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.db.backends': {
            'handlers': ['rotate'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

LOGGING_CONFIG = 'django.utils.log.dictConfig'
