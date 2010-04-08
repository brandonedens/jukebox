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
from footer import footer
from front import FrontScreen
from transient_message import transient_message


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

        self.set_size(settings.SCREEN_WIDTH,
                      settings.SCREEN_HEIGHT)

        # Setup screen container
        self.screen_container = ScreenContainer()
        self.add(self.screen_container)
        front = FrontScreen()
        self.screen_container.add_screen(front)
        self.screen_container.active_screen = front

        self.transient_message = transient_message
        self.footer = footer
        layout = self.get_layout_manager()
        layout.add(self.footer,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_END)
        self.add(transient_message)

    def on_press(self, actor, event):
        """
        Toplevel callback for when buttons are pressed.
        """
        if event.keyval == clutter.keysyms.Escape:
            logging.info('Escape button pressed. Quitting jukebox.')
            clutter.main_quit()
        elif event.keyval == clutter.keysyms.space:
            logging.debug('Space button pressed which means credit insert.')
            logging.info('Reading new credits value.')
            jukebox.credits_load()
            self.screen_container.update_screens()
        elif event.keyval == clutter.keysyms.d:
            logging.debug('Displaying footer.')
            self.footer.display()
        self.screen_container.on_press(actor, event)

    def on_release(self, actor, event):
        """
        Callback for when a button is released.

        Currently does nothing.
        """
        pass

    def on_second(self):
        """
        Callback heartbeat tick that arrives each second.
        """
        self.footer.update()
        self.screen_container.on_second()
        self.screen_container.update_screens()
        return True

    def set_transient_message(self, text):
        """
        Display a transient message.
        """
        self.transient_message.message(text)
        self.transient_message.raise_top()

