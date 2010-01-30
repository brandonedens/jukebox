# Brandon Edens
# 2010-01-09
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.views.generic.simple import direct_to_template


###############################################################################
## Functions
###############################################################################

def index(request):
    """
    """
    request.user.message_set.create(message="Welcome back %s." % request.user.first_name)
    request.user.message_set.create(message="How are you feeling today?")
    return direct_to_template(request, 'profile/index.html')

