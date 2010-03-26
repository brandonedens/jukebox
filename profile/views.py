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
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic.create_update import create_object, update_object
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

from jukebox.music.models import Artist, Photo, Song
from jukebox.music.forms import ArtistForm, PhotoForm, SongForm, TermsOfServiceForm


###############################################################################
## Functions
###############################################################################

@login_required
def index(request):
    """
    """
    artist_list = Artist.objects.filter(user=request.user)
    return direct_to_template(request, 'profile/index.html',
                              extra_context={'artist_list': artist_list},)

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
    return direct_to_template(request, 'profile/artist_form.html', {'form': form,})

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
                             template_name='profile/artist_form.html',
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
        return direct_to_template(request, 'profile/photo_form.html', {'form': form,})
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
        form = SongForm(request.POST, request.FILES, instance=song, prefix='song')
        tos = TermsOfServiceForm(request.POST, prefix='tos')
        tos_valid = tos.is_valid()
        if tos.is_valid() and form.is_valid():
            first_name = tos.cleaned_data['first_name'].strip().lower()
            last_name = tos.cleaned_data['last_name'].strip().lower()
            if first_name != request.user.first_name.strip().lower():
                tos.errors['first_name'] = "Firstname does not match user's firstname."
            elif last_name != request.user.last_name.strip().lower():
                tos.errors['last_name'] = "Lastname does not match user's lastname."
            else:
                song = form.save()
                return redirect_to(request, reverse('song_detail', args=[song.id]))
    else:
        tos = TermsOfServiceForm(initial={'first_name': 'first name',
                                          'last_name': 'last name'},
                                 prefix='tos')
        form = SongForm(instance=song, prefix='song')
    return direct_to_template(request, 'profile/song_form.html', {'form': form,
                                                                  'terms_of_service': tos})

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

@login_required
def song_play(request, song_id):
    """
    Return the song's data appropriate for playing.
    """
    song = get_object_or_404(Song, pk=song_id)
    if request.user == song.artist.user or request.user.is_superuser:
        # Open the song file and return it as response.
        print 'returning audio file.'
        response = HttpResponse(song.file.read(), mimetype='audio/mpeg')
        response['Accept-Ranges'] = "bytes"
        response['Content-Length'] = song.file.size
        response.status_code = 206
        #response.write(song.file.read())
        return response
    else:
        # Song is not owned by this user; do not allow play.
        request.user.message_set.create(
            message='This song does not belong to you. You cannot play it.'
            )
        return HttpResponseForbidden()

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
                         template_name='profile/song_form.html',
                         template_object_name='song')

