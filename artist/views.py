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
from django.views.generic.create_update import update_object
from django.views.generic.create_update import create_object
from django.views.generic.create_update import delete_object

from jukebox import settings
from jukebox.artist.forms import ArtistForm
from jukebox.artist.models import Artist


###############################################################################
## Functions
###############################################################################

@login_required
def create(request):
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
def delete(request, object_id):
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

def list_by_letter(request, letter):
    """
    Produce list of artists that start with the given letter.
    """
    artist_list = Artist.objects.filter(name__istartswith=letter)
    return object_list(request, queryset=artist_list,
                       template_object_name='artist',
                       paginate_by=settings.ARTISTS_PER_PAGE,)

@login_required
def update(request, object_id):
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

