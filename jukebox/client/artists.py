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

from jukebox.music.models import Artist

from symbols import LeftArrow, RightArrow
from header import Header
from screens import Screen, BlinkingText, ScrollingText
from songs import SongDetailScreen


###############################################################################
## Classes
###############################################################################

class ArtistText(clutter.Text):
    """
    """
    pass

class ArtistListScreen(Screen):

    def __init__(self):
        super(ArtistListScreen, self).__init__(clutter.BinLayout(
            clutter.BIN_ALIGNMENT_CENTER,
            clutter.BIN_ALIGNMENT_CENTER))
        self.set_name('artist list')
        layout = self.get_layout_manager()

        self.header = Header('All Artists')
        self.header.set_width(self.get_width())
        layout.add(self.header,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_START)

        self.left_arrow = LeftArrow()
        self.right_arrow = RightArrow()

        # Filter to all artists that have songs.
        artists = Artist.objects.filter(song__isnull=False).distinct().order_by('name')
        self.artists = ScrollingText(map(BlinkingText, artists),
                                     items_on_screen=settings.ARTIST_LIST_ITEMS)
        self.artists.set_width(self.get_width() -
                               (self.left_arrow.get_width() +
                                self.right_arrow.get_width()))
        self.artists.set_height(self.get_height() - self.header.get_height())

        layout.add(self.artists,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_CENTER)

        layout.add(self.left_arrow,
                   clutter.BIN_ALIGNMENT_START,
                   clutter.BIN_ALIGNMENT_CENTER)

        layout.add(self.right_arrow,
                   clutter.BIN_ALIGNMENT_END,
                   clutter.BIN_ALIGNMENT_CENTER)

    def on_press(self, actor, event):
        """
        """
        self.artists.on_press(actor, event)
        if event.keyval == clutter.keysyms.Left:
            self.get_parent().remove_screen(self)
        elif event.keyval == clutter.keysyms.Right:
            self.get_parent().new_screen(ArtistDetailScreen(self.artists.selected.obj))

class ArtistDetailScreen(Screen):

    def __init__(self, artist):
        super(ArtistDetailScreen, self).__init__(clutter.BinLayout(
            clutter.BIN_ALIGNMENT_CENTER,
            clutter.BIN_ALIGNMENT_CENTER))
        self.set_name('artist detail %s' % artist.name)
        layout = self.get_layout_manager()

        self.header = Header('Artist Details')
        self.header.set_width(self.get_width())
        layout.add(self.header,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_START)

        self.left_arrow = LeftArrow()

        songs = artist.song_set.all().order_by('title')
        self.songs = None
        if len(songs) > 0:
            self.right_arrow = RightArrow()
            self.songs = ScrollingText(map(BlinkingText,
                                           artist.song_set.all().order_by('title')),
                                       items_on_screen=settings.SONG_LIST_ITEMS)
            self.songs.set_width(self.get_width() -
                                 (self.left_arrow.get_width() +
                                  self.right_arrow.get_width()))
            self.songs.set_height(self.get_height() - self.header.get_height())
            layout.add(self.songs,
                       clutter.BIN_ALIGNMENT_CENTER,
                       clutter.BIN_ALIGNMENT_CENTER)
            layout.add(self.right_arrow,
                       clutter.BIN_ALIGNMENT_END,
                       clutter.BIN_ALIGNMENT_CENTER)

        else:
            text = clutter.Text('Router Bold 70', 'No songs available.')
            text.set_color(clutter.Color(200, 200, 200, 0xff))
            layout.add(text,
                       clutter.BIN_ALIGNMENT_CENTER,
                       clutter.BIN_ALIGNMENT_CENTER)

        layout.add(self.left_arrow,
                   clutter.BIN_ALIGNMENT_START,
                   clutter.BIN_ALIGNMENT_CENTER)


    def on_press(self, actor, event):
        """
        """
        if self.songs:
            self.songs.on_press(actor, event)

        if event.keyval == clutter.keysyms.Left:
            self.get_parent().remove_screen(self)
        if event.keyval == clutter.keysyms.Right:
            if self.songs:
                self.get_parent().new_screen(SongDetailScreen(self.songs.selected.obj))


