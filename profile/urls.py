# Brandon Edens
# 2010-01-27
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

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import update_object

from jukebox.profile.views import index
from jukebox.profile.views import artist_create, artist_delete, artist_update
from jukebox.profile.views import photo_upload
from jukebox.profile.views import song_create, song_delete, song_update, song_play

from jukebox.music.forms import ArtistForm


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.profile.views',
    url(r'^$', index, name='profile_index'),

    url(r'^artist/create/$', artist_create,
        name='artist_create'),
    url(r'^artist/update/(?P<object_id>\d+)/$', artist_update,
        name='artist_update',),
    url(r'^artist/delete/(?P<object_id>\d+)/$', artist_delete,
        name='artist_delete',),

    url(r'^photo/upload/(?P<artist_id>\d+)/$', photo_upload,
        name='photo_upload',),

    url(r'^song/create/(?P<artist_id>\d+)/$', song_create, name='song_create'),

    url(r'^song/play/(?P<song_id>\d+).mp3$', song_play, name='song_play'),

)

