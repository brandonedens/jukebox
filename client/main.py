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

import clutter
import logging

from jukebox.music.models import Song

from arrows import Arrow
from artists import ArtistsScreen
from config import config
from front import FrontScreen
from genres import Genres
from songs import SongsScreen


###############################################################################
## Constants
###############################################################################

ARROW_SIZE = 150


###############################################################################
## Classes
###############################################################################

class Jukebox(object):
    """
    """

    def __init__(self):
        """
        """

        # Setup initial variables.
        self.credits = 0
        self.admin_mode = False
        self.playing = None

        # Bring up clutter
        self.stage = clutter.Stage()
        # Hide the mouse cursor
        self.stage.hide_cursor()

        # Enable/disable fullscreen mode.
        if config.fullscreen:
            logging.info('Setting gui to fullscreen.')
            self.stage.set_fullscreen(True)
        else:
            logging.info('Setting gui to windowed mode.')

        self.screen_width = config.screen_width
        self.screen_height = config.screen_height
        logging.info("Resolution of screen is %d x %d." % (config.screen_width,
                                                           config.screen_height))
        self.stage.set_size(self.screen_width, self.screen_height)

        # Set stage background color to black
        self.stage.set_color(clutter.Color(0x00, 0x00, 0x00, 0xff))

        # Connect callback listeners
        self.stage.connect('destroy', clutter.main_quit)
        self.stage.connect('key-press-event', self.on_press)
        self.stage.connect('key-release-event', self.on_release)
        self.stage.connect('allocation-changed', self.on_allocation_changed)

        # Setup screens.
        self.screens = []
        self.active_screen = self.add_screen(FrontScreen())

    def on_allocation_changed(self, stage, allocation, flags):
        width, height = allocation.size
        #self.front.set_size(width, height)

    def on_press(self, actor, event):
        """
        Toplevel callback for when buttons are pressed.
        """
        if event.keyval == clutter.keysyms.Escape:
            logging.info('Escape button pressed. Quitting jukebox.')
            clutter.main_quit()

        elif event.keyval == clutter.keysyms.Left:
            if type(self.active_screen) == FrontScreen:
                # When front screen is active do not slide screens.
                return
            elif type(self.active_screen) in [SongsScreen]:
                logging.debug("active screen = %s" % self.active_screen)
                self.active_screen.slide_right()
                self.active_screen = self.screens[self.screens.index(self.active_screen) - 1]
                logging.debug("active screen = %s" % self.active_screen)
                self.active_screen.slide_right()

        elif event.keyval == clutter.keysyms.Right:
            if type(self.active_screen) == FrontScreen:
                self.active_screen.slide_left()
                selected = self.active_screen.get_selected()

                if selected == 'songs':
                    try:
                        screen = self.screens[1]
                        if type(screen) == SongsScreen:
                            # The next screen is a songs screen therefore we'll
                            # use that screen.
                            logging.debug('Found existing songs screen.')
                            self.active_screen = screen
                        else:
                            # Next screen is not songs screen so clear out all
                            # existing songs and add songs screen.
                            # FIXME add this functionality.
                            logging.debug('Next screen is not songs screen.')
                            pass
                    except IndexError:
                        # Could not access an existing songs screen so create a
                        # new one.
                        logging.debug('Creating new songs screen.')
                        self.active_screen = self.add_screen(SongsScreen(),
                                                             offscreen='right')
                else:
                    logging.error("Could not select a screen based upon front's selected entry.")
                self.active_screen.slide_left()
        elif type(self.active_screen) == SongsScreen:
            self.active_screen.slide_left()
            selected = self.active_screen.get_selected()
            try:
                screen = self.screens[2]

        self.active_screen.on_press(actor, event)

    def next_screen(self, current_screen, existing_screen=None, selected=None):
        """
        Given current screen and selected return the next screen to use.  If an
        existing screen is given then the system will check to see if the next
        screen is in fact that existing screen and if so then we simply return
        the existing screen.
        """
        next_screen = None
        if type(current_screen) == FrontScreen:
            if selected == 'songs':
                next_screen = SongsScreen
            elif selected == 'artists':
                next_screen = ArtistsScreen
            elif selected == 'genres':
                next_screen = GenresScreen
        elif type(current_screen) == SongsScreen:
            next_screen = SongScreen(selected)

        if next_screen == existing_screen:
            return existing_screen
        else:
            return

    def on_release(self, actor, event):
        """
        Toplevel callback for when keys are released.
        """
        pass

    def add_screen(self, screen, offscreen=None):
        """
        Add a screen to the current list of screens.
        """
        self.screens.append(screen)
        screen.set_size(self.stage.get_width(),
                        self.stage.get_height())
        self.stage.add(screen)

        if offscreen == 'right':
            screen.set_x(self.stage.get_width())
        elif offscreen == 'left':
            screen.set_x(-self.stage.get_width())
        else:
            screen.set_position(0, 0)
        return screen

    def run(self):
        self.stage.show()
        clutter.main()

