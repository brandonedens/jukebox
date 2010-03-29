# Brandon Edens
# 2010-03-11
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
from pango import ALIGN_CENTER

from jukebox.client.config import config


###############################################################################
## Constants
###############################################################################


###############################################################################
## Classes
###############################################################################

FONT_AS220 = 'Helvetica75Outline Bold 70'
FONT = 'Router Ultra-Bold Italic 30'
FONT_COLOR = clutter.Color(255, 255, 255)


###############################################################################
## Functions
###############################################################################

class Logo(clutter.Box):

    def __init__(self):
        super(Logo, self).__init__(clutter.BoxLayout())

        self.layout = self.get_layout_manager()
        self.layout.set_vertical(False)
        self.layout.set_spacing(30)

        self.set_color(clutter.Color(0, 0, 0, 230))

        self.as220 = clutter.Text(FONT_AS220, 'AS22O')
        self.as220.set_color(FONT_COLOR)
        self.jukebox = clutter.Text(FONT, 'Jukebox\nMusic')
        self.jukebox.set_color(FONT_COLOR)
        self.jukebox.set_line_alignment(ALIGN_CENTER)
        self.layout.pack(self.as220, False, False, False,
                         clutter.BOX_ALIGNMENT_CENTER,
                         clutter.BOX_ALIGNMENT_CENTER)
        self.layout.pack(self.jukebox, False, False, False,
                         clutter.BOX_ALIGNMENT_CENTER,
                         clutter.BOX_ALIGNMENT_CENTER)

