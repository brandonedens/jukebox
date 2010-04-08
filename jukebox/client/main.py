# Brandon Edens
# 2010-03-26
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
import clutter
import logging
import os
import shutil
import tempfile

from jukebox.music.models import QueuedPlay


###############################################################################
## Classes
###############################################################################

class Jukebox(object):
    """
    """

    def __init__(self):
        """
        """
        super(Jukebox, self).__init__()

        # Setup initial variables.
        self.credits = 0
        self.admin_mode = False
        self.playing = None

        self.credits_load()

    def can_buy_song(self):
        """
        Returns true or false if the user can buy a song.
        """
        if self.credits > 0:
            return True
        return False

    def credits_decrement(self):
        if self.credits > 0:
            self.credits -= 1
        self.credits_save()

    def credits_save(self):
        """
        """
        tmpfile = tempfile.NamedTemporaryFile()
        tmpfile.write("%d\n" % self.credits)
        tmpfile.flush()
        shutil.copy(tmpfile.name, settings.CREDITS_FILENAME)
        tmpfile.close()

    def credits_load(self):
        tmp_credits = 0
        if os.path.isfile(settings.CREDITS_FILENAME):
            fh = open(settings.CREDITS_FILENAME, 'r')
            try:
                tmp_credits = int(fh.readline())
            except ValueError:
                # Error reading the current credits value. Reset the system
                # back to 0.
                pass
            fh.close()
        self.credits = tmp_credits
        return self.credits

    def on_second(self):
        """
        Callback heartbeat tick that arrives each second.
        """
        logging.debug('One second heartbeat.')
        return True

    def song_buy(self, song):
        """
        Buy the named song.
        """
        logging.info('User bought song %s.' % song)
        # Decrement the available credits.
        self.credits_decrement()
        # Queue up the song to play
        queued_play = QueuedPlay(song=song)
        queued_play.save()


###############################################################################
## Statements
###############################################################################

# Create a single jukebox object.
jukebox = Jukebox()

