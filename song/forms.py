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

from django import forms
from django.core.urlresolvers import reverse

from jukebox.song.models import Song
from jukebox.utils.forms import ModelForm


###############################################################################
## Classes
###############################################################################

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('title',
                  'file',
                  )

    def clean_file(self):
        """
        Check that the digest is unique.
        """
        file = self.cleaned_data['file']
        # Check that file was mp3
        if file.content_type != 'audio/mpeg':
            raise forms.ValidationError('File uploaded is not a valid MP3 file.')
        # Check that the file's digest was unique
        digest = Song.digest_compute(file)
        try:
            song = Song.objects.get(digest=digest)
            if song:
                artist = song.artist
                txt = "The song \"%s\" by artist \"%s\" was already uploaded by user %s." % (song.title, artist.name, artist.user)
                raise forms.ValidationError(txt)
        except Song.DoesNotExist:
            pass
        return self.cleaned_data['file']

