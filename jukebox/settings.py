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
config = {}
# Find the configuration file.
for filename in CONFIG_FILE_LOCATIONS:
    if os.path.isfile(filename):
        config_file = open(filename, 'r')
        break
# Load the configuration file.
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

if config.get('media_root'):
    MEDIA_ROOT = config.get('media_root')

# Load client based settings from config file.

# important files
if config.get('credits_filename'):
    CREDITS_FILENAME = config.get('credits_filename')
if config.get('playing_filename'):
    PLAYING_FILENAME = config.get('playing_filename')
if config.get('last_song_filename'):
    LAST_SONG_FILENAME = config.get('last_song_filename')

# Logging settings
if config.get('log_format'):
    LOG_FORMAT = config.get('log_format')

if config.get('log_buttons_filename'):
    LOG_BUTTONS_FILENAME = config.get('log_buttons_filename')
if config.get('log_jukebox_filename'):
    LOG_JUKEBOX_FILENAME = config.get('log_jukebox_filename')
if config.get('log_player_filename'):
    LOG_PLAYER_FILENAME = config.get('log_player_filename')
if config.get('log_random_filename'):
    LOG_RANDOM_FILENAME = config.get('log_random_filename')


# Random play values
if config.get('random_sleep_min'):
    RANDOM_SLEEP_MIN = config.get('random_sleep_min')
if config.get('random_sleep_max'):
    RANDOM_SLEEP_MAX = config.get('random_sleep_max')
if config.get('random_no_play_start'):
    RANDOM_NO_PLAY_START = config.get('random_no_play_start')
if config.get('random_no_play_end'):
    RANDOM_NO_PLAY_END = config.get('random_no_play_end')
if config.get('random_play_volume'):
    RANDOM_PLAY_VOLUME = config.get('random_play_volume')
if config.get('paid_play_volume'):
    PAID_PLAY_VOLUME = config.get('paid_play_volume')


# Screen settings
if config.get('fullscreen'):
    FULLSCREEN = config.get('fullscreen')

if config.get('screen_width'):
    SCREEN_WIDTH = config.get('screen_width')

if config.get('screen_height'):
    SCREEN_HEIGHT = config.get('screen_height')

# Items list numbers
if config.get('artist_list_items'):
    ARTIST_LIST_ITEMS = config.get('artist_list_items')
if config.get('song_list_items'):
    SONG_LIST_ITEMS = config.get('song_list_items')

# Rate of blinking, moving, highlighting (in milliseconds)
if config.get('arrow_blink_rate'):
    ARROW_BLINK_RATE = config.get('arrow_blink_rate')
if config.get('blinking_text_rate'):
    BLINKING_TEXT_RATE = config.get('blinking_text_rate')
if config.get('footer_fade_rate'):
    FOOTER_FADE_RATE = config.get('footer_fade_rate')
if config.get('highlight_rate'):
    HIGHLIGHT_RATE = config.get('highlight_rate')
if config.get('screen_slide_rate'):
    SCREEN_SLIDE_RATE = config.get('screen_slide_rate')
if config.get('transient_message_fade_rate'):
    TRANSIENT_MESSAGE_FADE_RATE = config.get('transient_message_fade_rate')

# Font settings
if config.get('credits_font'):
    CREDITS_FONT = config.get('credits_font')
if config.get('footer_artist_font'):
    FOOTER_FONT = config.get('footer_artist_font')
if config.get('footer_song_font'):
    FOOTER_FONT = config.get('footer_song_font')
if config.get('footer_font'):
    FOOTER_FONT = config.get('footer_font')
if config.get('front_screen_font'):
    FRONT_SCREEN_FONT = config.get('front_screen_font')
if config.get('header_title_font'):
    HEADER_TITLE_FONT = config.get('header_title_font')
if config.get('logo_large_as220_font'):
    LOGO_AS220_LARGE_FONT = config.get('logo_as220_large_font')
if config.get('logo_large_jukebox_font'):
    LOGO_JUKEBOX_LARGE_FONT = config.get('logo_jukebox_large_font')
if config.get('logo_large_as220_font'):
    LOGO_AS220_SMALL_FONT = config.get('logo_as220_small_font')
if config.get('logo_large_jukebox_font'):
    LOGO_JUKEBOX_SMALL_FONT = config.get('logo_jukebox_small_font')
if config.get('scrolling_text_font'):
    SCROLLING_TEXT_FONT = config.get('scrolling_text_font')
if config.get('song_artist_font'):
    SONG_ARTIST_FONT = config.get('song_artist_font')
if config.get('song_title_font'):
    SONG_TITLE_FONT = config.get('song_title_font')
if config.get('transient_message_font'):
    TRANSIENT_MESSAGE_FONT = config.get('transient_message_font')

