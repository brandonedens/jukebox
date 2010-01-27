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

from jukebox.artist.models import Artist


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.artist.views',
    url(r'^$', object_list,
        {'queryset': Artist.objects.all(),
         'template_object_name': 'artist'},
        name='artist_list',),
    url(r'^detail/(?P<object_id>\d+)/$', object_detail,
        {'queryset': Artist.objects.all(),
         'template_object_name': 'artist'},
        name='artist_detail',),
)
