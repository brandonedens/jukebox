# Brandon Edens
# 2010-04-08
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
"""

###############################################################################
## Imports
###############################################################################

from django.conf import settings
import logging

from jukebox.client.models import QueuedPlay
from jukebox.music.models import Song


###############################################################################
## Functions
###############################################################################

def has_next_song():
    """
    Return True or False depending upon whether or not a next song will
    play.
    """
    if next_song():
        return True
    else:
        return False

def is_now_playing():
    """
    Return True or False depending upon whether or not a song is currently
    being played.
    """
    if now_playing():
        return True
    else:
        return False

def next_song():
    """
    """
    song = None
    if QueuedPlay.objects.count() > 1:
        queued_play = QueuedPlay.objects.all()[1]
        song = queued_play.song
    return song

def now_playing():
    """
    """
    song = None
    song = playing_load()
    return song

def playing_load():
    """
    Load the playing information from the filesystem. Return the song
    object associated with the playing song.
    """
    song = None
    try:
        fh = open(settings.PLAYING_FILENAME, 'r')
        song_id = int(fh.readline())
        fh.close()
        song = Song.objects.get(pk=song_id)
    except IOError:
        pass
    except Song.DoesNotExist:
        pass
    return song

def queue_song(song):
    """
    Queue the given song.
    """
    # Queue up the song to play
    queued_play = QueuedPlay(song=song, paid=True, random=False)
    queued_play.save()

