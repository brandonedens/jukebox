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

from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from django.db import models


###############################################################################
## Constants
###############################################################################


###############################################################################
## Functions
###############################################################################

def photo_upload_to(instance, filename):
    """
    Given an instance of a Photo, generate an appropriate storage location for
    that photo.
    """
    return "media/photos/%s/%s" % (instance.artist.name, filename)

def song_upload_to(instance, filename):
    """
    Given an instance of a Song, generate an appropriate storage location for
    that song.
    """
    return "media/songs/%s/%s" % (instance.artist.name, filename)

def video_upload_to(instance, filename):
    """
    Given an instance of a Video, generate an appropriate storage location for
    that video.
    """
    return "media/videos/%s/%s" % (instance.artist.name, filename)


###############################################################################
## Classes
###############################################################################

class Artist(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(
        help_text="""Description of the artist. This field uses Markdown to
 render the description. See: <a href="http://en.wikipedia.org/wiki/Markdown">
 Markdown on Wikipedia</a>.""")

    email_address = models.EmailField(
        help_text='Email address used to contact artist.')
    telephone_number = PhoneNumberField(
        help_text='Telephone number where the artist can be reached.')

    pay_to_the_order_of = models.CharField(
        max_length=128,
        help_text='Name the check should be made out to.')
    address1 = models.CharField(
        max_length=512,
        help_text='Address line 1 to mail check to.')
    address2 = models.CharField(
        max_length=512,
        blank=True,
        null=True,
        help_text='Address line 2 to mail check to.')
    city = models.CharField(
        max_length=128,
        help_text='The city portion of the address to mail check to.')
    state = USStateField(help_text='The state to mail check to.')
    zipcode = models.CharField(
        max_length=10,
        help_text='The zipcode that the check should be mailed to.')

    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        lower_name = self.name.lower()
        if lower_name.endswith(', the'):
            basename = self.name[:-5]
            the = self.name[-3:]
            return the+' '+basename
        else:
            return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('artist_detail', [str(self.id)])

    def random_photo(self):
        """
        Return random photo of the artist.
        """
        photo_set = self.photo_set.all()
        if photo_set:
            import random
            return photo_set[random.randint(0, len(photo_set)-1)]
        else:
            return None

    def save(self):
        """
        """
        lower_name = self.name.lower()
        if lower_name.startswith('the '):
            name = self.name
            basename = name[4:].strip()
            the = name[:3]
            name = basename + ', ' + the
            self.name = name
        super(Artist, self).save()

class Album(models.Model):
    user = models.ForeignKey(User)
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    user = models.ForeignKey(User)
    artist = models.ForeignKey(Artist)
    photo = models.ImageField(upload_to=photo_upload_to)
    caption = models.CharField(max_length=256, blank=True, null=True)

    thumbnail = models.ImageField(upload_to=photo_upload_to)

    # Whether or not the photo was reviewed.
    reviewed = models.BooleanField(default=False)

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (('can_review', 'Can review artist photos.'),)

    def __unicode__(self):
        return "%s - %s - %s" % (self.artist, self.photo, self.caption)

    def save(self):
        import os
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        THUMBNAIL_WIDTH = 300

        image = Image.open(self.photo)

        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        # Compute thumbnail height
        wpercent = (THUMBNAIL_WIDTH / float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))

        image.thumbnail((THUMBNAIL_WIDTH, hsize), Image.ANTIALIAS)

        temp_handle = StringIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.photo.name)[-1],
                                 temp_handle.read(), content_type='image/png')
        self.thumbnail.save(suf.name+'_thumbnail.png', suf, save=False)

        super(Photo, self).save()

class Song(models.Model):
    user = models.ForeignKey(User)
    artist = models.ForeignKey(Artist)

    title = models.CharField(
        max_length=200,
        help_text='The title of the song.'
        )
    file = models.FileField(
        upload_to=song_upload_to,
        help_text='File must be an MP3 and of reasonably high quality.')

    # Whether or not the song was reviewed.
    reviewed = models.BooleanField(default=False)

    # Number of times that the track was played.
    number_of_plays = models.PositiveIntegerField(default=0)
    # Number of random plays.
    number_of_random_plays = models.PositiveIntegerField(default=0)

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Audio specific model information
    bitrate = models.PositiveIntegerField()
    variable_bitrate = models.BooleanField()
    duration = models.PositiveIntegerField()
    sample_frequency = models.PositiveIntegerField()

    # File specific information
    digest = models.CharField(max_length=128, unique=True)

    class Meta:
        permissions = (('can_review', 'Can review songs.'),)

    def __unicode__(self):
        lower_title = self.title.lower()
        if lower_title.endswith(', the'):
            basetitle = self.title[:-5]
            the = self.title[-3:]
            return the+' '+basetitle
        else:
            return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('song_detail', [str(self.id)])

    def save(self):
        """
        """
        # Fix song characteristics.
        import eyeD3
        audio_file = eyeD3.Mp3AudioFile(self.file)
        tag = audio_file.getTag()

        # Set bitrate information.
        self.variable_bitrate, self.bitrate = audio_file.getBitRate()
        # Set duration of song in seconds.
        self.duration = audio_file.getPlayTime()
        # Set sample frequency.
        self.sample_frequency = audio_file.getSampleFreq()

        self.digest = self.digest_compute(self.file)

        # Correct the title.
        lower_title = self.title.lower()
        if lower_title.startswith('the '):
            title = self.title
            basetitle = title[4:].strip()
            the = title[:3]
            title = basetitle + ', ' + the
            self.title = title

        # Call parent save()
        super(Song, self).save()

    def get_previous(self):
        """
        Get the previous song by this song's artist.
        """
        song_list = list(self.artist.song_set.all())
        index = song_list.index(self)
        if index > 0:
            return song_list[index - 1]
        return None

    def get_next(self):
        """
        Get the previous song by this song's artist.
        """
        song_list = list(self.artist.song_set.all())
        index = song_list.index(self)
        if index < len(song_list) - 1:
            return song_list[index + 1]
        return None

    @classmethod
    def digest_compute(cls, file):
        """
        """
        import hashlib
        m = hashlib.sha512()
        m.update(file.read())
        return m.hexdigest()

class Video(models.Model):
    user = models.ForeignKey(User)
    artist = models.ForeignKey(Artist)
    video = models.FileField(upload_to=video_upload_to)
    caption = models.CharField(max_length=512)

    # Whether or not the video was reviewed.
    reviewed = models.BooleanField(default=False)

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.caption

class Website(models.Model):
    artist = models.ForeignKey(Artist)
    url = models.URLField()


