# Brandon Edens
# 2010-03-10
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

import datetime

from django.conf import settings
from django import http
from django.template import Context, loader
from django.views.generic.simple import direct_to_template

from jukebox.client.models import PaidPlay


###############################################################################
## Constants
###############################################################################


###############################################################################
## Classes
###############################################################################


###############################################################################
## Functions
###############################################################################

def generate_top_playlist(timedelta):
    """
    """
    now = datetime.datetime.now()
    plays = PaidPlay.objects.filter(played_on__gte=(now - timedelta))

    songs = {}
    for play in plays:
        if songs.has_key(play.song):
            songs[play.song] += 1
        else:
            songs[play.song] = 1
    songs_list = []
    for song in songs:
        songs_list.append((song, songs[song]))

    songs_list.sort(key=lambda x: x[1])
    songs_list.reverse()

    results = []
    for song in songs_list:
        results.append(song[0])

    return results


def index(request):
    """
    Initial index page.
    """
    day_previous = datetime.timedelta(hours=24)
    songs_most_played_today = generate_top_playlist(day_previous)
    week_previous = datetime.timedelta(days=7)
    songs_most_played_week = generate_top_playlist(week_previous)
    month_previous = datetime.timedelta(days=30)
    songs_most_played_month = generate_top_playlist(month_previous)

    now = datetime.datetime.now()
    paid_previous_plays = PaidPlay.objects.filter(played_on__gte=(now - week_previous))

    return direct_to_template(
        request, 'index.html',
        extra_context={'songs_most_played_today': songs_most_played_today,
                       'songs_most_played_week': songs_most_played_week[:10],
                       'songs_most_played_month': songs_most_played_month[:10],
                       'paid_previous_plays': paid_previous_plays,
                       },
        )

def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context:
        MEDIA_URL
            Path of static media (e.g. "media.example.org")
    """
    # You need to create a 500.html template.
    t = loader.get_template(template_name)
    return http.HttpResponseServerError(t.render(Context({
        'MEDIA_URL': settings.MEDIA_URL
    })))

