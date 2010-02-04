# Brandon Edens
# 2010-01-09
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

from jukebox import settings
from jukebox.artist.models import Artist
from jukebox.song.models import Song
from jukebox.song.forms import SongForm


###############################################################################
## Functions
###############################################################################

@login_required
def create(request, artist_id):
    """
    """
    artist = get_object_or_404(Artist, pk=artist_id)
    if request.user != artist.user:
        # Artist is not registered by the logged in user. This is an attempt at
        # fraud.
        request.user.message_set.create(
            message="You do not have permission to add songs to this artist."
            )
        return HttpResponseForbidden()
    song = Song(artist=artist)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            song = form.save()
            return redirect_to(request, reverse('song_detail', args=[song.id]))
    else:
        form = SongForm(instance=song)
    return direct_to_template(request, 'song/song_form.html', {'form': form,})

@login_required
def delete(request, object_id):
    """
    """
    song = get_object_or_404(Song, pk=object_id)
    if request.user != song.artist.user:
        # Song is not owned by this user. Do not allow them to delete this
        # song.
        request.user.message_set.create(
            message="This song does not belong to you. You do not have permission to delete it."
            )
        return HttpResponseForbidden()

def list_by_letter(request, letter):
    """
    Produce list of songs that start with the given letter.
    """
    song_list = Song.objects.filter(title__istartswith=letter)
    return object_list(request, queryset=song_list,
                       template_object_name='song',
                       paginate_by=settings.SONGS_PER_PAGE,)

@login_required
def update(request, object_id):
    """
    """
    pass

