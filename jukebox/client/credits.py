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
import shutil
import tempfile


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

        self.previous_credits = credits_load()
        self.credits = clutter.Text(settings.CREDITS_FONT, credits_load())
        self.credits.set_property('scale-gravity', clutter.GRAVITY_CENTER)
        self.credits.set_color(clutter.Color(255, 255, 255, 230))

        layout.pack(self.credits_text, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)
        layout.pack(self.credits, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)

    def update(self):
        """
        Update the credits information.
        """
        credits = credits_load()
        if credits != self.previous_credits:
            self.credits.set_text("%d" % credits)
            self.credits.set_scale(1.3, 1.3)
            self.credits.animate(clutter.LINEAR, settings.HIGHLIGHT_RATE,
                                 "scale-x", 1,
                                 "scale-y", 1,
                                 )
            self.previous_credits = credits

###############################################################################
## Functions
###############################################################################

def can_buy_song():
    """
    Returns true or false if the user can buy a song.
    """
    if credits_load() > 0:
        return True
    return False

def credits_decrement():
    credits = credits_load()
    if credits > 0:
        credits -= 1
    credits_save(credits)

def credits_save(value):
    """
    """
    tmpfile = tempfile.NamedTemporaryFile()
    tmpfile.write("%d\n" % value)
    tmpfile.flush()
    shutil.copy(tmpfile.name, settings.CREDITS_FILENAME)
    tmpfile.close()

def credits_load():
    tmp_credits = 0
    if os.path.isfile(settings.CREDITS_FILENAME):
        fh = open(settings.CREDITS_FILENAME, 'r')
        try:
            tmp_credits = int(fh.readline())
        except ValueError:
            # Error reading the current credits value. Reset the system
            # back to 0.
            pass
        fh.close()
    return tmp_credits

