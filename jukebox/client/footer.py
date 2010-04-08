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
import clutter

from playlist import is_now_playing, now_playing


###############################################################################
## Classes
###############################################################################

class Footer(clutter.Box):

    def __init__(self):
        super(Footer, self).__init__(clutter.BoxLayout())

        self.set_color(clutter.Color(0, 0, 0, 240))

        layout = self.get_layout_manager()
        layout.set_vertical(True)
        layout.set_spacing(20)

        self.set_width(settings.SCREEN_WIDTH)

        self.now_playing = clutter.Box(clutter.BoxLayout())
        tmplayout = self.now_playing.get_layout_manager()
        tmplayout.set_vertical(False)
        tmplayout.set_spacing(20)
        self.next_song = clutter.Box(clutter.BoxLayout())
        tmplayout = self.next_song.get_layout_manager()
        tmplayout.set_vertical(False)
        tmplayout.set_spacing(20)

        layout.pack(self.now_playing, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)
        layout.pack(self.next_song, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)


    def display(self):
        if jukebox.is_now_playing():
            song = jukebox.now_playing()
            text = clutter.Text(settings.FOOTER_TEXT, 'Now playing:')
            text.set_color(clutter.Color(200, 200, 200))
            self.now_playing.add(text)
            text = clutter.Text(settings.FOOTER_SONG_TEXT, song.title)
            text.set_color(clutter.Color(240, 240, 40))
            self.now_playing.add(text)
            try:
                print song.artist.name
            except jukebox.music.models.DoesNotExist:
                print 'got here'
            text = clutter.Text(settings.FOOTER_ARTIST_TEXT,
                                "by %s" % song.artist.name)
            text.set_color(clutter.Color(240, 240, 40))
            self.now_playing.add(text)

        if jukebox.has_next_song():
            song = jukebox.next_song()
            text = clutter.Text(settings.FOOTER_TEXT, 'Next song:')
            text.set_color(clutter.Color(200, 200, 200))
            self.next_song.add(text)
            text = clutter.Text(settings.FOOTER_SONG_TEXT, song.title)
            text.set_color(clutter.Color(240, 240, 40))
            self.next_song.add(text)
            artist = None
            text = clutter.Text(settings.FOOTER_ARTIST_TEXT,
                                "by %s" % song.artist.name)
            text.set_color(clutter.Color(240, 240, 40))
            self.next_song.add(text)

    def update(self):
        pass





###############################################################################
## Statements
###############################################################################

footer = Footer()

