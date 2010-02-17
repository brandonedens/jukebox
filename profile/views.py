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
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

from jukebox.music.models import Artist
from jukebox.music.forms import ArtistForm


###############################################################################
## Functions
###############################################################################

@login_required
def index(request):
    """
    """
    artist_list = Artist.objects.filter(user=request.user)
    request.user.message_set.create(message="Hello %s" % request.user.first_name)
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
            return redirect_to(request, reverse('artist_update', args=[artist.id]))
    else:
        form = ArtistForm(instance=artist)
    return direct_to_template(request, 'artist/artist_create_form.html', {'form': form,})

