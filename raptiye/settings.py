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
import os, sys

try:
    import django
except ImportError:
    sys.stderr.write("django couldn't be found.")
    sys.exit(1)

DOCUMENT_ROOT = os.path.abspath(os.path.dirname(__file__))
DJANGO_DIR = os.path.abspath(os.path.dirname(django.__file__))



# --- GENERIC SETTINGS ------------

PROJECT_NAME = u"raptiye"
VERSION = '2.2.2.1'
PROJECT_SUBTITLE = u"Quis custodes ipsos custodiet?"

COLORIZE_CODE = False
ENABLE_EMOTIONS = True
ENTRIES_PER_PAGE = 3

RSS_LIMIT = 10
RSS_URL = ""

BIRTH_DATE = date(1984, 05, 16)



# --- ADMIN SETTINGS --------------

ADMIN_LIST_PER_PAGE = 20



# --- COMMENT SETTINGS ------------

DISQUS_SHORTNAME = PROJECT_NAME



# --- TAG SETTINGS ----------------

FORCE_LOWERCASE_TAGS = True
MAX_TAG_LENGTH = 50



# --- USER ACCOUNT SETTINGS -------

# AUTH_PROFILE_MODULE = 'users.UserProfile'

# used by django-registration
# ACCOUNT_ACTIVATION_DAYS = 7



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

CSRF_COOKIE_DOMAIN = ".raptiye.org"

DEFAULT_CHARSET='utf-8'
DEFAULT_CONTENT_TYPE = 'text/html'
FILE_CHARSET = 'utf-8'

LOGIN_URL = "/users/login/"
LOGOUT_URL = "/users/logout/"
LOGIN_REDIRECT_URL = "/"
DEFAULT_AVATAR = lambda: MEDIA_URL + "template/images/default_avatar.png"

# URL Pattern Naming used here..
REDIRECT_URL = "blog"

INTERNAL_IPS = ()

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

MEDIA_ROOT = '%s/media/' % DOCUMENT_ROOT
MEDIA_URL = '/media/'
STATIC_URL = '/media/'

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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = 'raptiye.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "django.core.context_processors.csrf"
)

TEMPLATE_DIRS = (
    "%s/templates/default" % DOCUMENT_ROOT,
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader'
    )),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'tagging',
    # 'registration',
    # 'profiles',
    'raptiye.blog',
    'raptiye.contrib.flatpages',
    # 'raptiye.users',
)
