# Brandon Edens
# 2010-02-17
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

from django.contrib import admin

from jukebox.music.models import Artist, Album, Genre, Photo, Song


###############################################################################
## Classes
###############################################################################

class SongAdmin(admin.ModelAdmin):
    exclude = ('bitrate', 'variable_bitrate', 'duration', 'sample_frequency')


###############################################################################
## Functions
###############################################################################

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Photo)
admin.site.register(Song, SongAdmin)

