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
## Classes
###############################################################################

class Song(models.Model):

    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='songs/')

    reviewed = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

