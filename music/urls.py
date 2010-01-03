# Brandon Edens
# 2009-12-25
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
#
# This file is part of Jukebox.
#
# Jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Jukebox. If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

from django.conf.urls.defaults import *

from django.views.generic.create_update import delete_object
from django.views.generic.create_update import update_object
from django.views.generic.list_detail import object_detail
from django.views.generic.list_detail import object_list

from jukebox.music.models import Album
from jukebox.music.models import Artist
from jukebox.music.models import Genre
from jukebox.music.models import Song

from jukebox.music.forms import AlbumForm
from jukebox.music.forms import ArtistForm
from jukebox.music.forms import GenreForm
from jukebox.music.forms import SongForm

from jukebox.music.views import song_update
from jukebox.music.views import song_upload


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.music.views',

    # Song delete
    url(r'song/delete/(?P<object_id>\d+)/$',
        delete_object,
        {'model': Song,
         'post_delete_redirect': '/music/',
         'template_object_name': 'song'},
        name='song_delete'),

    # Song detail
    url(r'song/(?P<object_id>\d+)/$',
        object_detail,
        {'queryset': Song.objects.all(),
         'template_object_name': 'song'},
        name='song_details'),

    # Song list
    url(r'^$',
        object_list,
        {'queryset': Song.objects.all(),
         'template_object_name': 'song'},
        name='song_list'),

    # Song update
    url(r'^song/update/(?P<object_id>\d+)/$', 'song_update',
        name='song_update'),

    # Song upload
    url(r'^song/upload/$', song_upload, name='song_upload'),

)

