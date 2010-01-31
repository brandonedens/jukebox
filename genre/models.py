# Brandon Edens
# 2010-01-09
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.db import models


###############################################################################
## Classes
###############################################################################

class Genre(models.Model):
    name = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

