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
from django.views.generic.list_detail import object_detail
from django.views.generic.list_detail import object_list

from jukebox import settings
from jukebox.artist.models import Artist
from jukebox.artist.views import list_by_letter
from jukebox.artist.views import create, delete, update
from jukebox.artist.views import photo_upload


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.artist.views',
    url(r'^list/$', object_list,
        {'queryset': Artist.objects.all(),
         'template_object_name': 'artist',
         'paginate_by': settings.ARTISTS_PER_PAGE,},
        name='artist_list',),
    url(r'^list/startswith/(?P<letter>\w)/$', list_by_letter,
        name='artist_list_by_letter',),
    url(r'^detail/(?P<object_id>\d+)/$', object_detail,
        {'queryset': Artist.objects.all(),
         'template_object_name': 'artist'},
        name='artist_detail',),

    url(r'^create/$', create, name='artist_create'),
    url(r'^update/(?P<object_id>\d+)/$', update, name='artist_update',),
    url(r'^delete/(?P<object_id>\d+)/$', delete, name='artist_delete',),

    url(r'^photo_upload/(?P<artist_id>\d+)/$', photo_upload, name='photo_upload',),
)

