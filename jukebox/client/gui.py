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

from arrows import Arrow
from background import background
from config import config
from front import Front
from logo import Logo
from songs import Songs


###############################################################################
## Constants
###############################################################################

SCREEN_SLIDE_SPEED=200


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

        # Create a screen background image.
        background.set_size(self.screen_width, self.screen_height)
        #background.show()
        self.stage.add(background)
        background.lower_bottom()

        # Add the logo.
        self.logo = Logo()
        self.logo.show()

        # Add the front screen.
        self.front = Front()
        self.front.set_height(self.stage.get_height())
        self.front.show()
        self.stage.add(self.front)

        # Add the songs screen.
        self.songs = Songs()
        self.songs.set_position(self.screen_width, 20)
        self.songs.set_width(self.screen_width)
        self.songs.show()
        self.stage.add(self.songs)

        self.test = clutter.Box()
        self.test.set_position(350, 20)
        self.layout = clutter.FlowLayout()
        self.layout.set_homogeneous(True)
        self.layout.set_orientation(clutter.FLOW_HORIZONTAL)
        self.layout.set_column_spacing(10)
        self.layout.set_row_spacing(10)
        self.test.set_width(900)
        self.test.set_layout_manager(self.layout)
        self.test.show()
        self.stage.add(self.test)

        self.active_screen = self.front

        # Setup screen slide timeline
        self.screen_slide_timeline = clutter.Timeline(duration=SCREEN_SLIDE_SPEED)


    def on_press(self, actor, event):
        """
        """
        if event.keyval == clutter.keysyms.Escape:
            logging.info('Escape button pressed. Quitting jukebox.')
            clutter.main_quit()
        elif event.keyval == clutter.keysyms.Left:
            # Scroll in songs screen.
            path = clutter.Path()
            path.add_move_to(self.songs.get_x(), self.songs.get_y())
            path.add_line_to(self.screen_width, self.songs.get_y())
            alpha = clutter.Alpha(self.screen_slide_timeline, clutter.LINEAR)
            self.scroll_in = clutter.BehaviourPath(alpha, path)
            self.scroll_in.apply(self.songs)

            # Start timeline
            self.screen_slide_timeline.start()

        elif event.keyval == clutter.keysyms.Right:
            # Scroll in songs screen.
            path = clutter.Path()
            path.add_move_to(self.songs.get_x(), self.songs.get_y())
            path.add_line_to(self.front.get_width()+30, self.songs.get_y())
            alpha = clutter.Alpha(self.screen_slide_timeline, clutter.LINEAR)
            self.scroll_in = clutter.BehaviourPath(alpha, path)
            self.scroll_in.apply(self.songs)

            # Start timeline
            self.screen_slide_timeline.start()
        elif event.keyval == clutter.keysyms.g:
            group = clutter.Group()
            rect = clutter.Rectangle()
            rect.set_width(120)
            rect.set_height(100)
            rect.set_color(clutter.Color(0, 0, 0, 225))
            group.add(rect)
            text = clutter.Text('', 'Hello')
            text.set_color(clutter.Color(230, 230, 230))
            group.add(text)
            self.test.pack(group)
            #background.change('/home/brandon/Pictures/photo_booth/photo_2009-10-04T16-10-39_1.png')

        if self.active_screen:
            self.active_screen.on_press(actor, event)

    def run(self):
        self.stage.show()
        clutter.main()

