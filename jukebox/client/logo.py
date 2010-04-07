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

from django.conf import settings
from pango import ALIGN_CENTER
import clutter


###############################################################################
## Constants
###############################################################################


###############################################################################
## Classes
###############################################################################

FONT_COLOR = clutter.Color(255, 255, 255)


###############################################################################
## Functions
###############################################################################

class LogoLarge(clutter.Box):

    def __init__(self):
        super(LogoLarge, self).__init__(clutter.BoxLayout())

        layout = self.get_layout_manager()
        layout.set_vertical(False)
        layout.set_spacing(40)
        layout.set_use_animations(True)

        self.as220 = clutter.Text(settings.LOGO_AS220_LARGE_FONT,
                                  'AS22O')
        self.as220.set_color(FONT_COLOR)
        self.jukebox = clutter.Text(settings.LOGO_JUKEBOX_LARGE_FONT,
                                    'Jukebox\nMusic')
        self.jukebox.set_color(FONT_COLOR)
        self.jukebox.set_line_alignment(ALIGN_CENTER)
        layout.pack(self.as220, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)
        layout.pack(self.jukebox, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)

class LogoSmall(clutter.Box):

    def __init__(self):
        super(LogoSmall, self).__init__(clutter.BoxLayout())

        layout = self.get_layout_manager()
        layout.set_vertical(False)
        layout.set_spacing(20)
        layout.set_use_animations(True)

        self.as220 = clutter.Text(settings.LOGO_AS220_SMALL_FONT,
                                  'AS22O')
        self.as220.set_color(FONT_COLOR)
        self.jukebox = clutter.Text(settings.LOGO_JUKEBOX_SMALL_FONT,
                                    'Jukebox\nMusic')
        self.jukebox.set_color(FONT_COLOR)
        self.jukebox.set_line_alignment(ALIGN_CENTER)
        layout.pack(self.as220, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)
        layout.pack(self.jukebox, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)

