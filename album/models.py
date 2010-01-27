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

class Album(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=256)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

