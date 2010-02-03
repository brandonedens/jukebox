# Django settings for jukebox project.

import os
# Setup the directory name for this project.
DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Brandon Edens', 'brandon@as220.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = "%s/dev.db" % DIRNAME
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(DIRNAME, 'static_media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/jukebox/static_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g^okellta-s4ohpjo-b$0-7%m0qe2*smw-4xr1#a_zdv9%0@u^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django403.middleware.Django403Middleware',
)

ROOT_URLCONF = 'jukebox.urls'

TEMPLATE_DIRS = (
    DIRNAME + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',

    # Third party applications.
    'registration',

    # Local applications.
    'jukebox.utils',
    'jukebox.utils.templatetags',
    'jukebox.album',
    'jukebox.artist',
    'jukebox.artist.templatetags',
    'jukebox.genre',
    'jukebox.profile',
    'jukebox.song',
)

# URL to redirect to after successful login
LOGIN_REDIRECT_URL="/profile/"

# Days until registration activations expire
ACCOUNT_ACTIVATION_DAYS=7

# Email host
DEFAULT_FROM_EMAIL = "jukebox@as220.org"
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_USE_TLS = True

# Application specific settings

# Artist settings
ARTISTS_PER_PAGE = 6
SONGS_PER_PAGE = 6

