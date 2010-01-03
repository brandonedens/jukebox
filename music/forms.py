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

from django import forms
from django.forms import ModelForm

from jukebox.music.models import Album, Artist, Genre, Photo, Song


###############################################################################
## Constants
###############################################################################


###############################################################################
## Classes
###############################################################################

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('user', 'artist')

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user')

class GenreForm(ModelForm):
    class Meta:
        model = Genre

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ('artist', 'thumbnail')

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('title',)

class SongCreateForm(ModelForm):
    class Meta:
        model = Song
        fields = ('file',)

    def clean_file(self):
        """
        Check that the mime-type is mpeg a requirement for mp3 uploads.
        """
        import eyeD3
        file = self.cleaned_data['file']
        if file.content_type != 'audio/mpeg':
            raise forms.ValidationError("Not a valid MP3 file")
        return self.cleaned_data['file']


###############################################################################
## Functions
###############################################################################


