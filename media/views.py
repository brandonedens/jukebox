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

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

from jukebox import settings
from jukebox.media.models import Artist, Photo, Song


###############################################################################
## Classes
###############################################################################


###############################################################################
## Decorators
###############################################################################

def has_ownership(function=None, *args, **kwargs):
    """
    Check that the requesting user has ownership of the object.
    """
    return function(*args, **kwargs)


###############################################################################
## Functions
###############################################################################

def artist_list_by_letter(request, letter):
    """
    Produce list of artists that start with the given letter.
    """
    artist_list = Artist.objects.filter(name__istartswith=letter)
    return object_list(request, queryset=artist_list,
                       template_object_name='artist',
                       paginate_by=settings.ARTISTS_PER_PAGE,)

def song_list_by_letter(request, letter):
    """
    Produce list of songs that have title starting with the given letter.
    """
    song_list = Song.objects.filter(title__istartswith=letter)
    return object_list(request, queryset=song_list,
                       template_object_name='song',
                       paginate_by=settings.SONGS_PER_PAGE,)

@login_required
def artist_create(request):
    """
    Create a new artist.
    """
    artist = Artist(user=request.user)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect_to(request, reverse('artist_detail', args=[artist.id]))
    else:
        form = ArtistForm(instance=artist)
    return direct_to_template(request, 'artist/artist_form.html', {'form': form,})

@login_required
def artist_delete(request, object_id):
    """
    """
    artist = get_object_or_404(Artist, pk=object_id)
    if request.user == artist.user:
        return delete_object(request,
                             model=Artist,
                             object_id=artist.id,
                             post_delete_redirect=reverse('profile_index'))
    else:
        request.user.message_set.create(
            message="You do not have permission to delete this artist."
            )
        return HttpResponseForbidden()

@login_required
def artist_update(request, object_id):
    """
    """
    artist = get_object_or_404(Artist, pk=object_id)
    if request.user == artist.user:
        return update_object(request,
                             form_class=ArtistForm,
                             object_id=artist.id,
                             template_object_name='artist')
    else:
        request.user.message_set.create(
            message="You do not have permission to update this artist."
            )
        return HttpResponseForbidden()

@login_required
def photo_upload(request, artist_id):
    """
    Create a new photo.
    """
    artist = get_object_or_404(Artist, pk=artist_id)
    photo = Photo(artist=artist)
    if request.user == artist.user:
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES, instance=photo)
            if form.is_valid():
                photo = form.save()
                return redirect_to(request, reverse('artist_detail', args=[artist.id]))
        else:
            form = PhotoForm(instance=photo)
        return direct_to_template(request, 'artist/photo_form.html', {'form': form,})
    else:
        request.user.message_set.create(
            message="You do not have permission to upload photos for this artist."
            )
        return HttpResponseForbidden()

@login_required
def song_create(request, artist_id):
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
def song_delete(request, object_id):
    """
    """
    song = get_object_or_404(Song, pk=object_id)
    if request.user != song.artist.user:
        # Song is not owned by this user. Do not allow delete.
        request.user.message_set.create(
            message="This song does not belong to you. You do not have permission to delete it."
            )
        return HttpResponseForbidden()
    return delete_object(request,
                         model=Song,
                         object_id=song.id,
                         post_delete_redirect=reverse('song_detail', args=[song.artist.id]))

def song_play(request, object_id):
    """
    Return the song's data appropriate for playing.
    """
    song = get_object_or_404(Song, pk=object_id)
    if request.user != song.artist.user:
        # Song is not owned by this user; do not allow play.
        request.user.message_set.create(
            message='This song does not belong to you. You cannot play it.'
            )
        return HttpResponseForbidden()
    # Open the song file and return it as response.
    response = HttpResponse(mimetype='audio/mpeg')
    response.write(song.file.read())
    return response

@login_required
def song_update(request, object_id):
    """
    """
    song = get_object_or_404(Song, pk=object_id)
    if request.user != song.artist.user:
        # Song is not owned by this user; do not allow update.
        request.user.message_set.create(
            message='This song does not belong to you. You cannot update it.'
            )
        return HttpResponseForbidden()
    return update_object(request,
                         form_class=SongForm,
                         object_id=song.id,
                         template_object_name='song')


