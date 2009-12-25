# Brandon Edens
# AS220
# 2009-12-24
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
# along with Jukebox.  If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin


###############################################################################
## Statements
###############################################################################

admin.autodiscover()

urlpatterns = patterns('',

    # Administrative services.
    (r'^admin/', include(admin.site.urls)),

    # Registration URLs.
    (r'^accounts/', include('registration.urls')),

    # Music application URLs.
    (r'^music/', include('music.urls')),

    # Browsing music URLs.
    (r'^browse/', include('browse.urls')),

    # Local URLS.
    (r'^$', 'jukebox.views.index'),
    (r'^profile/$', 'jukebox.views.profile'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^jukebox/static_media/(?P<path>.*)$', 'serve',
     {'document_root': '/home/brandon/src/jukebox/static_media',
      'show_indexes': True }),)

