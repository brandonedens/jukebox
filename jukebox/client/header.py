# Brandon Edens
# 2010-03-31
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

from logo import LogoSmall
from credits import Credits


###############################################################################
## Constants
###############################################################################

FONT_COLOR = clutter.Color(150, 150, 255)


###############################################################################
## Classes
###############################################################################

class Header(clutter.Box):

    def __init__(self, title):
        super(Header, self).__init__(
            clutter.BinLayout(clutter.BIN_ALIGNMENT_CENTER,
                              clutter.BIN_ALIGNMENT_START,)
            )
        layout = self.get_layout_manager()
        #layout.set_vertical(False)

        # Setup default header elements.
        self.logo = LogoSmall()
        self.title = clutter.Text(settings.HEADER_TITLE_FONT, title)
        self.title.set_color(FONT_COLOR)
        self.credits = Credits()
        layout.add(self.logo,
                   clutter.BIN_ALIGNMENT_START,
                   clutter.BIN_ALIGNMENT_START)
        layout.add(self.title,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_START)
        layout.add(self.credits,
                   clutter.BIN_ALIGNMENT_END,
                   clutter.BIN_ALIGNMENT_START)

    def update(self):
        """
        Update the contents of oneself, specifically the credits information.
        """
        print 'called header update.'
        self.credits.update()

