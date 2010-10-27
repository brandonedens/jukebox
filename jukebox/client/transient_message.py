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
from pango import ALIGN_CENTER
import clutter
import logging


###############################################################################
## Classes
###############################################################################

class TransientMessage(clutter.Box):

    def __init__(self):
        super(TransientMessage, self).__init__(
            clutter.BinLayout(clutter.BIN_ALIGNMENT_CENTER,
                              clutter.BIN_ALIGNMENT_CENTER))
        self.set_size(settings.SCREEN_WIDTH,
                      settings.SCREEN_HEIGHT)
        self.set_color(clutter.Color(0, 0, 0, 0))
        self.text = clutter.Text(settings.TRANSIENT_MESSAGE_FONT, '')
        self.text.set_property('scale-gravity', clutter.GRAVITY_CENTER)
        self.text.set_line_alignment(ALIGN_CENTER)
        self.text.set_line_wrap(True)
        self.text.set_color(clutter.Color(230, 230, 230))
        self.add(self.text)
        self.animation = None

    def message(self, text, color=None):
        logging.info("Setting transient message to %s" % text)
        self.set_color(clutter.Color(0, 0, 0))
        self.set_opacity(250)
        self.text.set_text(text)
        if color:
            self.text.set_color(color)
        else:
            self.text.set_color(clutter.Color(230, 230, 230))
        self.animation = self.animate(clutter.EASE_IN_CUBIC,
                                      settings.TRANSIENT_MESSAGE_FADE_RATE,
                                      'opacity', 0)

###############################################################################
## Statements
###############################################################################

# The global transient message
transient_message = TransientMessage()

