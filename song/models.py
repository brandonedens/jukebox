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

    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_to)

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

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('song_detail', [str(self.id)])

    def save(self):
        import eyeD3
        audio_file = eyeD3.Mp3AudioFile(self.file)
        tag = audio_file.getTag()

        # Set bitrate information.
        self.variable_bitrate, self.bitrate = audio_file.getBitRate()
        # Set duration of song in seconds.
        self.duration = audio_file.getPlayTime()
        # Set sample frequency.
        self.sample_frequency = audio_file.getSampleFreq()

        # Call parent save()
        super(Song, self).save()

