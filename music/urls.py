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
from django.views.generic.create_update import update_object
from django.views.generic.list_detail import object_detail

from jukebox.music.forms import SongForm
from jukebox.music.models import Song
from jukebox.music.views import song_upload


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.music.views',
    # Object detail
    (r'song/(?P<object_id>\d+)/$',
     object_detail,
     {'queryset': Song.objects.all()}),
    # Song update
    (r'song/update/(?P<object_id>\d+)/$',
     update_object,
     {'form_class': SongForm,}),
    # Song upload
    (r'^song/upload/$', song_upload),
)


