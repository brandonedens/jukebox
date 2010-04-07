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

ARROW_SIZE = 150


###############################################################################
## Classes
###############################################################################

class Jukebox(clutter.Box):
    """
    """

    def __init__(self):
        """
        """
        super(Jukebox, self).__init__(clutter.FixedLayout())

        # Setup initial variables.
        self.credits = 0
        self.admin_mode = False
        self.playing = None

        # Setup screens.
        self.screens = []
        self.active_screen = self.add_screen(FrontScreen())

    def on_press(self, actor, event):
        """
        Toplevel callback for when buttons are pressed.
        """
        if event.keyval == clutter.keysyms.Escape:
            logging.info('Escape button pressed. Quitting jukebox.')
            clutter.main_quit()
        self.active_screen.on_press(actor, event)

    def on_signal(self, signum, frame):
        """
        Handler for incoming process signals.
        """

    def on_release(self, actor, event):
        """
        Toplevel callback for when keys are released.
        """
        pass

    def clear_screens(self, current_screen):
        """
        Removes all screens after the current_screen.
        """
        while self.screens[-1] != current_screen:
            # Pop a screen off the stack.
            screen = self.screens.pop()
            logging.debug("Clearing screen %s." % screen)
            # Remove the screen from the box.
            self.remove(screen)

    def new_screen(self, new_screen):
        """
        Add a screen to the current list of screens slide that screen to the
        foreground.

        If the new_screen already exists in the list of screens then simply
        activate the existing version of that screen.
        """
        current_screen_index = self.screens.index(self.active_screen)
        next_screen = None
        try:
            next_screen = self.screens[current_screen_index + 1]
        except IndexError:
            pass

        if next_screen and next_screen.get_name() == new_screen.get_name():
            # We have existing screen so simply use that one.
            self.active_screen.slide_left()
            self.active_screen = next_screen
            self.active_screen.slide_left()
        else:
            self.clear_screens(self.active_screen)
            self.active_screen.slide_left()
            self.active_screen = self.add_screen(new_screen, 'right')
            self.active_screen.slide_left()

    def remove_screen(self, screen):
        """
        Remove a screen which really means sliding the current screen out of
        the way moving the virtual camera to the left. We leave the previous
        screen in the screen's list in case the user immediately wants to
        return to that screen.
        """
        self.active_screen.slide_right()
        self.active_screen = self.screens[self.screens.index(screen) - 1]
        self.active_screen.slide_right()

    def add_screen(self, screen, offscreen=None):
        """
        Add a screen to the current list of screens.
        """
        self.screens.append(screen)
        self.add(screen)
        if offscreen == 'right':
            screen.set_x(settings.SCREEN_WIDTH)
        elif offscreen == 'left':
            screen.set_x(-settings.SCREEN_WIDTH)
        else:
            screen.set_position(0, 0)
        return screen

