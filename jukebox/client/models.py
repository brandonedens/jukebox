# Brandon Edens
# 2010-04-09
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

from jukebox.music.models import Song
from django.db import models


###############################################################################
## Classes
###############################################################################

class CoinInsert(models.Model):
    """
    The coin insert model.
    """
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('added_on',)

class QueuedPlay(models.Model):
    """
    The playlist queue.
    """
    song = models.ForeignKey(Song)

    paid = models.BooleanField(default=False)
    random = models.BooleanField(default=False)

    added_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('added_on',)

    def __unicode__(self):
        return "%s - %s - %s" % (self.added_on, self.song.artist, self.song)

    def __str__(self):
        return self.__unicode__()

class RandomPlay(models.Model):
    """
    Model that represents when a song was randomly played.
    """
    song = models.ForeignKey(Song)
    played_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('played_on',)

    def __unicode__(self):
        try:
            return "%s - %s - %s" % (self.played_on, self.song.artist, self.song)
        except Song.DoesNotExist:
            print "Error: Could not find the song for random play %s." % self.id
            return ""

    def __str__(self):
        return self.__unicode__()

class PaidPlay(models.Model):
    """
    Model that represents when a song was randomly played.
    """
    song = models.ForeignKey(Song)
    played_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('played_on',)

    def __unicode__(self):
        try:
            return "%s - %s - %s" % (self.played_on, self.song.artist, self.song)
        except Song.DoesNotExist:
            print "Error: Could not find the song for paid play %s." % self.id
            return ""

    def __str__(self):
        return self.__unicode__()

