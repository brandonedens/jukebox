# Brandon Edens
# 2010-01-09
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.contrib.auth.models import User
from django.db import models


###############################################################################
## Functions
###############################################################################

def upload_to(instance, filename):
    """
    Given an instance of a Photo or Video as well as the filename, generate an
    appropriate storage location for this photo.
    """
    return "artist/%s/%s" % (instance.artist.name, filename)


###############################################################################
## Classes
###############################################################################

class Artist(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()

    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
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

class Website(models.Model):
    artist = models.ForeignKey(Artist)
    url = models.URLField()

class Photo(models.Model):
    artist = models.ForeignKey(Artist)
    image = models.ImageField(upload_to=upload_to)
    caption = models.CharField(max_length=256, blank=True, null=True)

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s - %s" % (self.artist, self.image, self.caption)

class Video(models.Model):
    artist = models.ForeignKey(Artist)
    video = models.FileField(upload_to=upload_to)
    caption = models.CharField(max_length=512)

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.caption

