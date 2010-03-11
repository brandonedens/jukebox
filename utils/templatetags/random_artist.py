# Brandon Edens
# 2010-02-19
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
Template tag to get a random artist.
"""

###############################################################################
## Imports
###############################################################################

import random

from django import template

register = template.Library()

from jukebox import settings
from jukebox.music.models import Photo


###############################################################################
## Constants
###############################################################################


###############################################################################
## Classes
###############################################################################

class RandomArtistNode(template.Node):

    def __init__(self):
        photo_set = Photo.objects.all()
        self.photo = photo_set[random.randint(0, len(photo_set)-1)]
        self.artist = self.photo.artist

    def render(self, context):
        if self.photo:
            file_url = ""+settings.MEDIA_URL+self.photo.thumbnail.file
            print file_url
            txt = ""
            txt += "<a href=\""+self.artist.get_absolute_url+"\">"
            #txt += "<img src=\""+self.photo.thumbnail.file+"\" />"
            txt += "</a>"
            return txt
        else:
            return ""


###############################################################################
## Functions
###############################################################################

def random_artist(parser, token):
    return RandomArtistNode()

register.tag('random_artist', random_artist)

