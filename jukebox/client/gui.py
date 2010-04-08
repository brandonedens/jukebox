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
import clutter
import logging

from screens import ScreenContainer
from front import FrontScreen


###############################################################################
## Classes
###############################################################################

class GUI(clutter.Box):
    """
    Main GUI for the jukebox.
    """

    def __init__(self):
        """
        """
        super(GUI, self).__init__(
            clutter.BinLayout(clutter.BIN_ALIGNMENT_CENTER,
                              clutter.BIN_ALIGNMENT_CENTER)
            )

        # Setup screen container
        self.screen_container = ScreenContainer()
        self.add(self.screen_container)
        front = FrontScreen()
        self.screen_container.add_screen(front)
        self.screen_container.active_screen = front

    def on_press(self, actor, event):
        """
        Toplevel callback for when buttons are pressed.
        """
        if event.keyval == clutter.keysyms.Escape:
            logging.info('Escape button pressed. Quitting jukebox.')
            clutter.main_quit()
        self.screen_container.on_press(actor, event)

    def on_release(self, actor, event):
        """
        Callback for when a button is released.

        Currently does nothing.
        """
        pass

