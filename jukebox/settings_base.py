# Brandon Edens
# 2010-03-17
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
#
# This file is part of jukebox.
#
# jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with jukebox. If not, see <http://www.gnu.org/licenses/>.
"""
Base settings for all forms that the jukebox web software might be used.

When deploying the jukebox web software creating a settings.py file and
overload the settings here as necessary.
"""

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Brandon Edens', 'brandon@as220.org'),
    ('Xander Marro', 'xander@as220.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = "dev.db"
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

# Site name
SITE_NAME = 'AS220 Jukebox'

# Site URL
SITE_URL = 'http://as220.org/jukebox_dev/'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/brandon/src/jukebox/static_media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/jukebox/static_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

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
    '/home/brandon/src/jukebox/templates',
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
    'jukebox.music',
    'jukebox.music.templatetags',
    'jukebox.profile',
    'jukebox.review',
    'jukebox.search',
)

# URL to redirect to after successful login
LOGIN_REDIRECT_URL="/profile/"

# Days until registration activations expire
ACCOUNT_ACTIVATION_DAYS=7

# Email host
DEFAULT_FROM_EMAIL = "jukebox@as220.org"
SERVER_EMAIL = "jukebox-admin@as220.org"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
EMAIL_USE_TLS = True

# Application specific settings

# Artist settings
ARTISTS_PER_PAGE = 6
SONGS_PER_PAGE = 6

# Uploaded file settings
#FILE_UPLOAD_MAX_MEMORY_SIZE = 0



################################################################################
## Client related settings
################################################################################

LOG_FILENAME = '/tmp/jukebox.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

FULLSCREEN = True
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

ARTIST_LIST_ITEMS = 10
SONG_LIST_ITEMS = 10

ARROW_BLINK_RATE = 1000
BLINKING_TEXT_RATE = 800
HIGHLIGHT_RATE = 600
SCREEN_SLIDE_RATE = 300

HEADER_TITLE_FONT = 'Router Bold 50'
LOGO_AS220_LARGE_FONT = 'Helvetica75Outline Bold 120'
LOGO_JUKEBOX_LARGE_FONT = 'Router Ultra-Bold Italic 55'
LOGO_AS220_SMALL_FONT = 'Helvetica75Outline Bold 50'
LOGO_JUKEBOX_SMALL_FONT = 'Router Ultra-Bold Italic 20'
SCROLLING_TEXT_FONT = 'Router Bold Italic 40'
SONG_ARTIST_FONT = 'Router Bold Italic 30'
SONG_TITLE_FONT = 'Router Bold 70'


