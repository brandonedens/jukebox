# Brandon Edens
# 2010-03-12
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

from logo import LogoLarge
from screens import Screen
from symbols import RightArrow

from songs import SongListScreen
from artists import ArtistListScreen
from genres import GenreListScreen


###############################################################################
## Constants
###############################################################################

ARROW_SIZE = 150

BLINK_RATE = 800
HIGHLIGHT_RATE = 600

FONT_COLOR = clutter.Color(200, 200, 200)
FONT_OPACITY = 80


###############################################################################
## Classes
###############################################################################

class FrontScreen(Screen):

    def __init__(self):
        super(FrontScreen, self).__init__(clutter.BoxLayout())

        layout = self.get_layout_manager()
        layout.set_use_animations(True)
        layout.set_vertical(True)
        layout.set_spacing(20)

        self.logo = LogoLarge()
        layout.pack(self.logo, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)

        self.labels = (
            clutter.Text(settings.FRONT_SCREEN_FONT, 'songs'),
            clutter.Text(settings.FRONT_SCREEN_FONT, 'artists'),
            )

        self.selected = self.labels[0]

        for label in self.labels:
            label.set_color(FONT_COLOR)
            label.set_opacity(FONT_OPACITY)
            label.set_property('scale-gravity', clutter.GRAVITY_CENTER)
            layout.pack(label, True, False, False,
                        clutter.BOX_ALIGNMENT_CENTER,
                        clutter.BOX_ALIGNMENT_CENTER)

        self.set_color(clutter.Color(0, 0, 0, 225))
        #self.set_color(clutter.Color(90, 0, 0, 200))
        self.highlight(self.selected)

        self.right_arrow = RightArrow(ARROW_SIZE)
        self.add(self.right_arrow)

        self.right_arrow.set_position(self.get_width() - ARROW_SIZE,
                                      self.get_height()/2 - ARROW_SIZE/2,
                                      )
        self.right_arrow.blink_on()

    def on_timeline_completed(self, timeline, behaviour):
        """
        """
        behaviour.remove_all()

    def get_selected(self):
        """
        """
        return self.selected.get_text()

    def highlight(self, actor):
        """
        """
        actor.animate(clutter.LINEAR, HIGHLIGHT_RATE,
                      "opacity", 255,
                      "scale-x", 1.3,
                      "scale-y", 1.3,
                      )

    def blink(self, actor):
        animation = actor.animate(clutter.LINEAR, BLINK_RATE,
                                  'color', clutter.Color(255, 0, 0, 255))
        animation.connect_after('completed', self.on_blink_completed, actor)
        #animation.set_loop(True)

    def unhighlight(self, actor):
        """
        """
        actor.animate(clutter.LINEAR, HIGHLIGHT_RATE,
                      "scale-x", 1,
                      "scale-y", 1,
                      "opacity", FONT_OPACITY,
                      )

    def on_blink_completed(self, animation, actor):
        if actor.get_color() == clutter.Color(255, 0, 0, 255):
            animation = actor.animate(clutter.LINEAR, BLINK_RATE,
                                       'color', clutter.Color(0, 255, 0, 255))
        elif actor.get_color() == clutter.Color(0, 255, 0, 255):
            animation = actor.animate(clutter.LINEAR, BLINK_RATE,
                                       'color', clutter.Color(0, 0, 255, 255))
        elif actor.get_color() == clutter.Color(0, 0, 255, 255):
            animation = actor.animate(clutter.LINEAR, BLINK_RATE,
                                       'color', clutter.Color(255, 0, 0, 255))

        animation.connect_after('completed', self.on_blink_completed, actor)

    def on_press(self, actor, event):
        """
        Keyboard button press callback.
        """
        if event.keyval == clutter.keysyms.Up:
            index = self.labels.index(self.selected)
            if index > 0:
                self.unhighlight(self.selected)
                self.selected = self.labels[index - 1]
                self.highlight(self.selected)

        elif event.keyval == clutter.keysyms.Down:
            index = self.labels.index(self.selected)
            if index < len(self.labels) - 1:
                self.unhighlight(self.selected)
                self.selected = self.labels[index + 1]
                self.highlight(self.selected)

        elif event.keyval == clutter.keysyms.Right:
            if self.selected.get_text() == 'songs':
                self.get_parent().new_screen(SongListScreen())
            elif self.selected.get_text() == 'artists':
                self.get_parent().new_screen(ArtistListScreen())

