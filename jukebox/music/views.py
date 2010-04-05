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

from jukebox import settings
from jukebox.music.models import Artist, Genre, Photo, Song


###############################################################################
## Classes
###############################################################################


###############################################################################
## Decorators
###############################################################################

#def tmp(test):
#    def decorate(view_func):
#        return view_func
#    return decorate

#def has_ownership(function=None, model='TEST'):
#    """
#    Check that the requesting user has ownership of the object.
#    """
#    actual_decorator = tmp(lambda u: print 'lambda')
#    if function:
#        return actual_decorator(function)
#    return actual_decorator
#     if model:
#         print 'have model'
#     def decorate(*args, **kwargs):
#         if function:
#             return function(*args, **kwargs)
#     return decorate


###############################################################################
## Functions
###############################################################################

def index(request):
    """
    Index for the music page.
    """
    artist_list = Artist.objects.all()
    song_list = Song.objects.all()
    genre_list = Genre.objects.all()
    return direct_to_template(request, 'music/index.html',
                              extra_context={'artist_list': artist_list,
                                             'song_list': song_list,
                                             'genre_list': genre_list,},)

def artist_list_by_letter(request, letter):
    """
    Produce list of artists that start with the given letter.
    """
    artist_list = Artist.objects.filter(startswith=letter.lower())
    return object_list(request, queryset=artist_list,
                       template_object_name='artist',
                       paginate_by=settings.ARTISTS_PER_PAGE,)

def song_list_by_letter(request, letter):
    """
    Produce list of songs that have title starting with the given letter.
    """
    song_list = Song.objects.filter(startswith=letter.lower())
    return object_list(request, queryset=song_list,
                       template_object_name='song',
                       paginate_by=settings.SONGS_PER_PAGE,)


