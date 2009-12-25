# Brandon Edens
# AS220
# 2009-12-24
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
#
# This file is part of Jukebox.
#
# Jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Jukebox.  If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

from django.contrib.auth.models import User
from django.db import models

from jukebox import settings


###############################################################################
## Classes
###############################################################################

class Artist(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200, unique=True)
    website = models.URLField(null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    user = models.ForeignKey(User)
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=200)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Genre(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class Photo(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images/artists/")
    thumbnail = models.ImageField(upload_to="images/artist_thumbnails/", editable=False)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        THUMBNAIL_SIZE = (100, 100)

        image = Image.open(self.photo.file)

        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        temp_handle = StringIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.photo.name)[-1],
                               temp_handle.read(), content_type='image/png')
        self.thumbnail.save(suf.name+'.png', suf, save=False)

        super(Photo, self).save()

    def __unicode__(self):
        return self.title

class Song(models.Model):
    user = models.ForeignKey(User)
    artist = models.ForeignKey(Artist, null=True)
    album = models.ForeignKey(Album, null=True)
    genre = models.ForeignKey(Genre, null=True )

    file = models.FileField(upload_to='songs/')
    title = models.CharField(max_length=200)

    # Bitrate information
    bitrate = models.PositiveIntegerField()
    variable_bitrate = models.BooleanField()

    duration = models.PositiveIntegerField()
    sample_frequency = models.PositiveIntegerField()

    track_number = models.PositiveSmallIntegerField(null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/music/song/%i/" % self.id

    def save(self):
        import eyeD3
        audio_file = eyeD3.Mp3AudioFile(settings.MEDIA_ROOT+'songs/'+self.file.name)
        tag = audio_file.getTag()

        # Set bitrate information.
        (self.variable_bitrate, self.bitrate) = audio_file.getBitRate()
        # Set duration of song in seconds.
        self.duration = audio_file.getPlayTime()
        # Set sample frequency.
        self.sample_frequency = audio_file.getSampleFreq()

        # If tag exists attempt to extract information from it.
        if tag:
            # Populate the song title if its not already set.
            if not self.title:
                self.title = tag.getTitle()
            # Gather track information
            if not self.track_number:
                self.track_number = tag.getTrackNum()

            if not self.artist:
                # Handle populating the artist field
                artist_name = tag.getArtist()
                try:
                    print self.user
                    self.artist = Artist.objects.get(name=artist_name, user=self.user)
                except Artist.DoesNotExist:
                    artist = Artist(name=artist_name, user=self.user)
                    artist.save()
                    self.artist = artist

            if not self.album:
                # Handle album
                album_title = tag.getAlbum()
                try:
                    self.album = Album.objects.get(title=album_title, user=self.user)
                except Album.DoesNotExist:
                    album = Album(title=album_title, user=self.user, artist=self.artist)
                    album.save()
                    self.album = album

            if not self.genre:
                # Gather genre information
                eyeD3Genre = tag.getGenre()
                genre_name = eyeD3Genre.getName()
                try:
                    self.genre = Genre.objects.get(name=genre_name)
                except Genre.DoesNotExist:
                    genre = Genre(name=genre_name)
                    genre.save()
                    self.genre = genre

        super(Song, self).save()

    def __unicode__(self):
        return self.title

