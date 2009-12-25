# Brandon Edens
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
# along with Jukebox. If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

from django.views.generic.simple import direct_to_template


###############################################################################
## Functions
###############################################################################

# Default index
def index(request):
    return direct_to_template(request, 'index.html')

# Default page after login
def profile(request):
    songs = request.user.song_set.all()
    return direct_to_template(request, 'profile.html', {'songs': songs,})

