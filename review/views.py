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
from django.core.mail import send_mail, mail_admins
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template, redirect_to

from jukebox.music.models import Song, Photo
from jukebox.review.forms import RejectForm


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
    song.approved = True
    song.save()
    song.artist.user.message_set.create(
        message="Your song %s was reviewed and will be inserted into the jukebox." % song)

    return redirect_to(request, reverse('review_songs'))

@login_required
@permission_required('music.song.can_review')
def song_reject(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'POST':
        form = RejectForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            # Create the reason message
            message = "Your song \"%s\" was reviewed and not approved for reason: %s" % (song, reason)
            # Send the message to the user.
            user = song.artist.user
            user.message_set.create(message=message)
            # Create an email to send to user.
            mail_subject = "Song \"%s\" not approved for AS220 Jukebox" % song
            mail_from = "jukebox@as220.org"
            mail_rcpt = [song.artist.user.email]
            send_mail(mail_subject, message, mail_from, mail_rcpt, fail_silently=True)
            message += "\nFor artist \"%s\" created by user %s %s aka %s." % (song.artist,
                                                                              user.first_name,
                                                                              user.last_name,
                                                                              user.username)
            mail_admins(mail_subject, message, fail_silently=True)
            song.reviewed = True
            song.approved = False
            song.save()
            return redirect_to(request, reverse('review_songs'))
    else:
        form = RejectForm()
    return direct_to_template(request,
                              'review/reject_reason.html',
                              {'form': form,
                               'song': song,
                               },)
