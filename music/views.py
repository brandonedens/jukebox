# Create your views here.


###############################################################################
## Imports
###############################################################################

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

from jukebox.music.forms import AlbumForm, ArtistForm, GenreForm, SongCreateForm, SongForm
from jukebox.music.models import Song


###############################################################################
## Functions
###############################################################################

def song_update(request, object_id):
    """
    Update an existing song.
    """
    song = get_object_or_404(Song, pk=object_id)
    artist = song.artist
    album = song.album
    genre = song.genre

    if request.method == 'POST':
        song_form = SongForm(request.POST, prefix='song', instance=song)
        song_valid = song_form.is_valid()
        artist_form = ArtistForm(request.POST, prefix='artist', instance=artist)
        artist_valid = artist_form.is_valid()
        album_form = AlbumForm(request.POST, prefix='album', instance=album)
        album_valid = album_form.is_valid()
        genre_form = GenreForm(request.POST, prefix='genre', instance=genre)
        genre_valid = genre_form.is_valid()

        if album_valid and artist_valid and genre_valid and song_valid:
            # Perform temporary saves.
            artist = artist_form.save()
            genre = genre_form.save()
            album = album_form.save(commit=False)
            song = song_form.save(commit=False)

            # Save the album information
            album.artist = artist
            album.save()

            # Save the song information
            song.album = album
            song.artist = artist
            song.genre = genre
            song.save()
            return redirect_to(request, reverse('song_details', args=[song.id]))
    else:
        album_form = AlbumForm(instance=album, prefix='album')
        artist_form = ArtistForm(instance=artist, prefix='artist')
        genre_form = GenreForm(instance=genre, prefix='genre')
        song_form = SongForm(instance=song, prefix='song')
    return direct_to_template(request,
                              'music/song_form.html',
                              {'album_form': album_form,
                               'artist_form': artist_form,
                               'genre_form': genre_form,
                               'song_form': song_form,})

def song_upload(request):
    """
    Upload a song.
    """
    song = Song(user=request.user)
    if request.method == 'POST':
        form = SongCreateForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect_to(request, reverse('song_list'))
    else:
        form = SongCreateForm(instance=song)
    return direct_to_template(request, 'music/song_upload_form.html', {'form': form,})

