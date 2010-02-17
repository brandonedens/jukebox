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

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail
from django.views.generic.list_detail import object_list

from jukebox import settings
from jukebox.media.models import Artist, Photo, Song
from jukebox.media.views import artist_list_by_letter, song_list_by_letter
from jukebox.media.views import artist_create, artist_update, artist_delete
from jukebox.media.views import photo_upload
from jukebox.media.views import song_create, song_update, song_delete, song_play


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.media.views',
    url(r'^artist/list/$', object_list,
        {'queryset': Artist.objects.all(),
         'template_object_name': 'artist',
         'paginate_by': settings.ARTISTS_PER_PAGE,},
        name='artist_list',),
    url(r'^artist/list/startswith/(?P<letter>\w)/$', artist_list_by_letter,
        name='artist_list_by_letter',),
    url(r'^artist/detail/(?P<object_id>\d+)/$', object_detail,
        {'queryset': Artist.objects.all(),
         'template_object_name': 'artist'},
        name='artist_detail',),

    url(r'^artist/create/$', artist_create,
        name='artist_create'),
    url(r'^artist/update/(?P<object_id>\d+)/$', artist_update,
        name='artist_update',),
    url(r'^artist/delete/(?P<object_id>\d+)/$', artist_delete,
        name='artist_delete',),

    url(r'^photo/upload/(?P<artist_id>\d+)/$', photo_upload,
        name='photo_upload',),

    url(r'^song/list/$', object_list,
        {'queryset': Song.objects.all(),
         'template_object_name': 'song',
         'paginate_by': settings.SONGS_PER_PAGE,},
        name='song_list',),
    url(r'^song/list/startswith/(?P<letter>\w)/$', song_list_by_letter,
        name='song_list_by_letter',),
    url(r'^song/detail/(?P<object_id>\d+)/$', object_detail,
        {'queryset': Song.objects.all(),
         'template_object_name': 'song'},
        name='song_detail',),

    url(r'^song/create/(?P<artist_id>\d+)/$', song_create, name='song_create'),

    url(r'^song/play/(?P<object_id>\d+)/$', song_play, name='song_play'),
)

