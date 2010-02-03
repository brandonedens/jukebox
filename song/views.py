# Brandon Edens
# 2010-01-09
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.views.generic.list_detail import object_list

from jukebox import settings
from jukebox.song.models import Song


###############################################################################
## Functions
###############################################################################

def list_by_letter(request, letter):
    """
    Produce list of songs that start with the given letter.
    """
    song_list = Song.objects.filter(title__istartswith=letter)
    return object_list(request, queryset=song_list,
                       template_object_name='song',
                       paginate_by=settings.SONGS_PER_PAGE,)

