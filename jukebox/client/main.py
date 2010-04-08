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

from jukebox.music.models import Song

from front import FrontScreen


###############################################################################
## Constants
###############################################################################


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

    def decrement_credits(self):
        current_credits = read_credits()
        current_credits -= 1
        if current_credits < 0:
            # current credits cannot go below 0
            current_credits = 0
        fh = open(settings.CREDITS_FILENAME, 'w')
        fh.write("%d\n" % current_credits())
        fh.close()
        self.credits = current_credits

    def read_credits(self):
        current_credits = 0
        if os.path.isfile(settings.CREDITS_FILENAME):
            fh = open(settings.CREDITS_FILENAME, 'r')
            try:
                current_credits = int(fh.readline())
            except ValueError:
                # Error reading the current credits value. Reset the system
                # back to 0.
                pass
            fh.close()
        self.credits = current_credits
        return current_credits


###############################################################################
## Statements
###############################################################################

# Create a single jukebox object.
jukebox = Jukebox()

