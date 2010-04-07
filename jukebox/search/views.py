# Brandon Edens
# 2010-01-09
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.views.generic.simple import direct_to_template\

from jukebox.music.models import Artist, Song, Genre
from jukebox.search.forms import SearchForm


###############################################################################
## Functions
###############################################################################

def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            terms = search.split(' ')
            # Exact matches
            artist_list = Artist.objects.filter(name__icontains=search)
            song_list = Song.objects.filter(title__icontains=search)

            # Partial matches
            for term in terms:
                artist_list = artist_list | Artist.objects.filter(
                    name__icontains=term
                    )
                song_list = song_list | Song.objects.filter(
                    title__icontains=term
                    )

            genre_list = Genre.objects.filter(name__icontains=search)
            return direct_to_template(request, template='search/results.html',
                                      extra_context={
                                          'artist_list': artist_list,
                                          'song_list': song_list,
                                          'genre_list': genre_list,
                                          'form': form,
                                          },)
    else:
        form = SearchForm()
    return direct_to_template(request, 'search/search_form.html',
                              {'form': form,})

