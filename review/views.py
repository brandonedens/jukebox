# Brandon Edens
# 2010-01-09
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template, redirect_to

from jukebox.music.models import Song, Photo


###############################################################################
## Functions
###############################################################################

@login_required
@permission_required('music.song.can_review')
def index(request):
    song_list = Song.objects.filter(reviewed=False)
    photo_list = Photo.objects.filter(reviewed=False)
    return direct_to_template(request, template='review/index.html',
                              extra_context={
                                  'song_list': song_list,
                                  'photo_list': photo_list,
                                  },)

@login_required
@permission_required('music.song.can_review')
def song_accept(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.reviewed = True
    song.save()
    song.artist.user.message_set.create(message="Your song %s was approved." % song)

    return redirect_to(request, reverse('review_songs'))

@login_required
@permission_required('music.song.can_review')
def song_reject(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.reviewed = False
    song.save()
    return redirect_to(request, reverse('review_songs'))

