# Django settings for jukebox project.

# Load the base settings.
from settings_base import *

# We're going to attempt to read configuration from a configuration file on the
# filesystem stored in YAML format.
import yaml
import os
CONFIG_FILE_LOCATIONS = [os.getenv('HOME')+'/.jukebox.rc',
                         '/etc/jukebox/jukebox.conf',
                         ]
config_file = None
config = {}#yaml.load("data: False")
for filename in CONFIG_FILE_LOCATIONS:
    if os.path.isfile(filename):
        config_file = open(CONFIG_FILENAME, 'r')
        break
if config_file:
    config = yaml.load(config_file)

# Load database settings from config file.
if config.get('database_engine'):
    DATABASE_ENGINE = config.get('database_engine')
if config.get('database_name'):
    DATABASE_NAME = config.get('database_name')
if config.get('database_user'):
    DATABASE_USER = config.get('database_user')
if config.get('database_password'):
    DATABASE_PASSWORD = config.get('database_password')
if config.get('database_host'):
    DATABASE_HOST = config.get('database_host')
if config.get('database_port'):
    DATABASE_PORT = config.get('database_port')

# Load client based settings from config file.
if config.get('fullscreen'):
    FULLSCREEN = config.get('fullscreen')

if config.get('screen_width'):
    SCREEN_WIDTH = config.get('screen_width')

if config.get('screen_height'):
    SCREEN_HEIGHT = config.get('screen_height')

if config.get('log_filename'):
    LOG_FILENAME = config.get('log_filename')

if config.get('log_format'):
    LOG_FORMAT = config.get('log_format')

