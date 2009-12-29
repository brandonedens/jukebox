# Create your views here.


###############################################################################
## Imports
###############################################################################

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

from jukebox.music.forms import SongCreateForm
from jukebox.music.models import Song


###############################################################################
## Functions
###############################################################################

def song_update(request):
    """
    Update an existing song.
    """
    pass

def song_upload(request):
    """
    Upload a song.
    """
    song = Song(user=request.user)
    if request.method == 'POST':
        form = SongCreateForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect_to(request, reverse('jukebox.views.profile'))
    else:
        form = SongCreateForm(instance=song)
    return direct_to_template(request, 'song_form.html', {'form': form,})

