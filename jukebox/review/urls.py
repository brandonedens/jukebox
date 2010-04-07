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

from jukebox.review.views import index
from jukebox.review.views import song_accept, song_reject
from django.views.generic.list_detail import object_list

from jukebox.music.models import Song, Photo


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.review.views',
    url(r'^$', index, name='review_index',),
    url(r'^songs/$', object_list,
        {'queryset': Song.objects.filter(reviewed=False).order_by(
            'uploaded_on'
            ),
         'template_name': 'review/review_song_list.html',
         'template_object_name': 'song',
         'paginate_by': 10,},
        name='review_songs',),
    url(r'^song/accept/(?P<song_id>\d+)/$', song_accept, name='song_accept',),
    url(r'^song/reject/(?P<song_id>\d+)/$', song_reject, name='song_reject',),
)


