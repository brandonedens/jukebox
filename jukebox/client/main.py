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

from jukebox.music.models import Song, QueuedPlay


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

        self.credits_load()


    def on_second(self):
        """
        Callback heartbeat tick that arrives each second.
        """
        logging.debug('One second heartbeat.')
        return True



###############################################################################
## Statements
###############################################################################

# Create a single jukebox object.
#jukebox = Jukebox()

