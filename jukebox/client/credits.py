# Brandon Edens
# 2010-04-07
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
import os

from main import jukebox


###############################################################################
## Constants
###############################################################################

FONT_COLOR = clutter.Color(220, 220, 150)


###############################################################################
## Classes
###############################################################################

class Credits(clutter.Box):

    def __init__(self):
        super(Credits, self).__init__(clutter.BoxLayout())
        layout = self.get_layout_manager()
        layout.set_vertical(False)
        layout.set_spacing(20)

        self.credits_text = clutter.Text(settings.CREDITS_FONT, 'Credits:')
        self.credits_text.set_color(FONT_COLOR)

        self.credits = clutter.Text(settings.CREDITS_FONT, jukebox.read_credits())
        self.credits.set_color(clutter.Color(255, 255, 255, 230))

        layout.pack(self.credits_text, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)
        layout.pack(self.credits, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)

