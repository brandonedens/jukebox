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
from django.views.generic.list_detail import object_list

from jukebox.music.models import Artist


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.browse.views',
    (r'^$', object_list, {'queryset': Artist.objects.all()}),
)


###############################################################################
## Classes
###############################################################################


###############################################################################
## Functions
###############################################################################


