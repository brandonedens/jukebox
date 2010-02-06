# Brandon Edens
# 2010-01-09
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.db import models

from jukebox.artist.models import Artist


###############################################################################
## Functions
###############################################################################

def upload_to(instance, filename):
    """
    Given an instance of a Song as well as the filename, generate an
    appropriate storage location for this song.
    """
    return "songs/%s/%s" % (instance.artist.name, filename)


###############################################################################
## Classes
###############################################################################

class Song(models.Model):
    artist = models.ForeignKey(Artist)

    title = models.CharField(
        max_length=200,
        help_text='The title of the song.'
        )
    file = models.FileField(
        upload_to=upload_to,
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

