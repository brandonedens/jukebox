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

from django.contrib.localflavor.us.forms import USZipCodeField
from django import forms

from jukebox.music.models import Artist, Photo, Song
from jukebox.utils.forms import ModelForm


###############################################################################
## Classes
###############################################################################

class ArtistForm(ModelForm):
    zipcode = USZipCodeField()

    class Meta:
        model = Artist
        exclude = ('user', 'slug', 'startswith')

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', 'caption',)

class TermsOfServiceForm(forms.Form):
    agree = forms.BooleanField(required=True)
    first_name = forms.CharField(min_length=1,
                                 widget=forms.TextInput(attrs={'size':'10'}))
    last_name = forms.CharField(min_length=1,
                                widget=forms.TextInput(attrs={'size':'10'}))

    def clean_agree(self):
        """
        Check that terms of service was checked.
        """
        print 'got to clean agree'
        agree = self.cleaned_data['agree']
        if not agree:
            raise forms.ValidationError(
                "Cannot upload a file unless terms of service is agreed to."
                )
        return self.cleaned_data['agree']

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'file',)

