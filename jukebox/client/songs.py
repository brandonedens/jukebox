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
from pango import ALIGN_CENTER
import clutter
import logging

from jukebox.client.models import QueuedPlay
from jukebox.music.models import Song

from header import Header
from screens import Screen, BlinkingText, ScrollingText
from symbols import BuySymbol, LeftArrow, RightArrow
from transient_message import transient_message
from credits import can_buy_song, credits_decrement
from playlist import queue_song


###############################################################################
## Classes
###############################################################################

class SongListScreen(Screen):

    def __init__(self):
        super(SongListScreen, self).__init__(clutter.BinLayout(
            clutter.BIN_ALIGNMENT_CENTER,
            clutter.BIN_ALIGNMENT_CENTER))
        self.set_name('song list')
        layout = self.get_layout_manager()

        self.header = Header('All Songs')
        self.header.set_width(self.get_width())
        layout.add(self.header,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_START)

        self.left_arrow = LeftArrow()
        self.right_arrow = RightArrow()

        songs = Song.objects.filter(approved=True).order_by('title')
        self.songs = ScrollingText(map(BlinkingText, songs),
                                   items_on_screen=settings.SONG_LIST_ITEMS)
        self.songs.set_width(self.get_width() -
                             (self.left_arrow.get_width() +
                              self.right_arrow.get_width()))
        self.songs.set_height(self.get_height() - self.header.get_height())

        layout.add(self.songs,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_END)

        layout.add(self.left_arrow,
                   clutter.BIN_ALIGNMENT_START,
                   clutter.BIN_ALIGNMENT_CENTER)

        layout.add(self.right_arrow,
                   clutter.BIN_ALIGNMENT_END,
                   clutter.BIN_ALIGNMENT_CENTER)

    def on_second(self):
        """
        """
        pass

    def on_press(self, actor, event):
        """
        """
        self.songs.on_press(actor, event)
        if event.keyval == clutter.keysyms.Left:
            self.get_parent().remove_screen(self)
        elif event.keyval == clutter.keysyms.Right:
            self.get_parent().new_screen(
                SongDetailScreen(self.songs.selected.obj)
                )

class SongDetailScreen(Screen):

    def __init__(self, song):
        super(SongDetailScreen, self).__init__(clutter.BinLayout(
            clutter.BIN_ALIGNMENT_CENTER,
            clutter.BIN_ALIGNMENT_CENTER))
        # Immediately store song information
        self.song = song
        self.set_name('song detail %s' % self.song.title)
        layout = self.get_layout_manager()

        self.header = Header('Song Details')
        self.header.set_width(self.get_width())
        layout.add(self.header,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_START)

        self.left_arrow = LeftArrow()
        self.buy = BuySymbol()

        self.box = clutter.Box(clutter.BoxLayout())
        box_layout = self.box.get_layout_manager()
        box_layout.set_vertical(True)
        box_layout.set_spacing(20)
        text = clutter.Text(settings.SONG_TITLE_FONT, self.song.title)
        text.set_line_alignment(ALIGN_CENTER)
        text.set_line_wrap(True)
        text.set_color(clutter.Color(230, 230, 230, 0xff))
        self.box.add(text)
        text = clutter.Text(
            settings.SONG_ARTIST_FONT, "by %s" % self.song.artist.name
            )
        text.set_line_alignment(ALIGN_CENTER)
        text.set_line_wrap(True)
        text.set_color(clutter.Color(210, 210, 210, 0xff))
        self.box.add(text)
        self.box.set_width(self.get_width() -
                           (self.left_arrow.get_width() +
                            self.buy.get_width()))


        layout.add(self.box,
                   clutter.BIN_ALIGNMENT_CENTER,
                   clutter.BIN_ALIGNMENT_CENTER,)

        layout.add(self.left_arrow,
                   clutter.BIN_ALIGNMENT_START,
                   clutter.BIN_ALIGNMENT_CENTER)

        layout.add(self.buy,
                   clutter.BIN_ALIGNMENT_END,
                   clutter.BIN_ALIGNMENT_CENTER)


    def on_press(self, actor, event):
        """
        """
        if event.keyval == clutter.keysyms.Left:
            self.get_parent().remove_screen(self)
        elif event.keyval == clutter.keysyms.Return:
            if can_buy_song():
                logging.info('User bought song %s.' % self.song)
                queue_song(self.song)
                credits_decrement()
                transient_message.message('Bought song %s' % self.song,
                                          color=clutter.Color(40, 250, 40))
                self.header.update()
            else:
                transient_message.message('Insert Quarter!',
                                          color=clutter.Color(250, 40, 40))

    def update(self):
        """
        """
        self.header.update()

