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
import logging

from playlist import is_now_playing, now_playing, has_next_song, next_song


###############################################################################
## Classes
###############################################################################

class Footer(clutter.Box):

    def __init__(self):
        super(Footer, self).__init__(clutter.BoxLayout())

        self.set_color(clutter.Color(0, 0, 0, 0))

        layout = self.get_layout_manager()
        layout.set_vertical(True)
        layout.set_spacing(20)

        self.set_width(settings.SCREEN_WIDTH)

        self.now_playing = now_playing()

        self.now_playing_box = clutter.Box(clutter.BoxLayout())
        tmplayout = self.now_playing_box.get_layout_manager()
        tmplayout.set_vertical(False)
        tmplayout.set_spacing(20)
        self.next_song_box = clutter.Box(clutter.BoxLayout())
        tmplayout = self.next_song_box.get_layout_manager()
        tmplayout.set_vertical(False)
        tmplayout.set_spacing(20)

        layout.pack(self.now_playing_box, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)
        layout.pack(self.next_song_box, True, False, False,
                    clutter.BOX_ALIGNMENT_CENTER,
                    clutter.BOX_ALIGNMENT_CENTER)


    def display(self):
        if is_now_playing() and self.now_playing != now_playing():
            self.now_playing = now_playing()
            self.set_color(clutter.Color(0, 0, 0, 250))
            self.set_opacity(250)

            # Remove existing text.
            for actor in self.now_playing_box.get_children():
                self.now_playing_box.remove(actor)

            song = now_playing()
            text = clutter.Text(settings.FOOTER_FONT, 'Now playing:')
            text.set_color(clutter.Color(200, 200, 200))
            self.now_playing_box.add(text)
            text = clutter.Text(settings.FOOTER_SONG_FONT, song)
            text.set_color(clutter.Color(240, 240, 40))
            self.now_playing_box.add(text)
            try:
                text = clutter.Text(settings.FOOTER_ARTIST_FONT,
                                    "by %s" % song.artist)
                text.set_color(clutter.Color(240, 240, 40))
                self.now_playing_box.add(text)
            except Exception:
                pass

            if has_next_song():
                song = next_song()

                # Remove existing text.
                for actor in self.next_song_box.get_children():
                    self.next_song_box.remove(actor)

                text = clutter.Text(settings.FOOTER_FONT, 'Next song:')
                text.set_color(clutter.Color(200, 200, 200))
                self.next_song_box.add(text)
                text = clutter.Text(settings.FOOTER_SONG_FONT, song)
                text.set_color(clutter.Color(240, 240, 40))
                self.next_song_box.add(text)
                try:
                    text = clutter.Text(settings.FOOTER_ARTIST_FONT,
                                        "by %s" % song.artist)
                    text.set_color(clutter.Color(240, 240, 40))
                    self.next_song_box.add(text)
                except Exception:
                    pass

            self.animation = self.animate(clutter.EASE_IN_CUBIC,
                                          settings.FOOTER_FADE_RATE,
                                          'opacity', 0)

    def update(self):
        self.display()


###############################################################################
## Statements
###############################################################################

footer = Footer()

