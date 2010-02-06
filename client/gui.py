# Brandon Edens
# 2010-02-06
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

import logging

import clutter

from jukebox.client.config import config


###############################################################################
## Constants
###############################################################################


###############################################################################
## Classes
###############################################################################

class GUI:

    def __init__(self):
        # Bring up clutter
        self.stage = clutter.Stage()
        # Hide the mouse cursor
        self.stage.hide_cursor()

        # Enable/disable fullscreen mode.
        if config.fullscreen:
            logging.debug('Setting gui to fullscreen.')
            self.stage.set_fullscreen(True)
        else:
            logging.debug("Setting gui to windowed mode with %d x %d."
                          % (config.screen_width, config.screen_height))
            self.stage.set_size(config.screen_width, config.screen_height)

    def run(self):
        self.stage.show()
        clutter.main()


###############################################################################
## Functions
###############################################################################


