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
from jukebox.music.models import Artist, Genre, Photo, Song
from jukebox.music.views import index
from jukebox.music.views import artist_list_by_letter, song_list_by_letter


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.music.views',
    url(r'^$', index, name='music_index',),

    url(r'^artist/$', object_list,
        {'queryset': Artist.objects.filter(song__approved=True).distinct(),
         'template_object_name': 'artist',
         'paginate_by': settings.ARTISTS_PER_PAGE,},
        name='artist_list',),
    url(r'^artist/startswith/(?P<letter>\w)/$', artist_list_by_letter,
        name='artist_list_by_letter',),
    url(r'^artist/(?P<object_id>\d+)/$', object_detail,
        {'queryset': Artist.objects.filter(song__approved=True).distinct(),
         'template_object_name': 'artist'},
        name='artist_detail',),

    url(r'^song/$', object_list,
        {'queryset': Song.objects.filter(approved=True),
         'template_object_name': 'song',
         'paginate_by': settings.SONGS_PER_PAGE,},
        name='song_list',),
    url(r'^song/startswith/(?P<letter>\w)/$', song_list_by_letter,
        name='song_list_by_letter',),
    url(r'^song/(?P<object_id>\d+)/$', object_detail,
        {'queryset': Song.objects.filter(),
         'template_object_name': 'song'},
        name='song_detail',),

    url(r'^genre/$', object_list,
        {'queryset': Genre.objects.all(),
         'template_object_name': 'genre',},
        name='genre_list'),
    url(r'^genre/(?P<object_id>\d+)/$', object_detail,
        {'queryset': Genre.objects.all(),
         'template_object_name': 'genre'},
        name='genre_detail'),
)

