# Brandon Edens
# 2010-01-09
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
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
    description = models.TextField(help_text='Description of the artist. This field uses Markdown to render the description. See: <a href="http://en.wikipedia.org/wiki/Markdown">Markdown on Wikipedia</a>.')


    email_address = models.EmailField(help_text='Email address used to contact artist.')
    telephone_number = PhoneNumberField(help_text='Telephone number where the artist can be reached.')

    pay_to_the_order_of = models.CharField(max_length=128,
                                           help_text='Name the check should be made out to.')
    address1 = models.CharField(max_length=512,
                                help_text='Address line 1 to mail check to.')
    address2 = models.CharField(max_length=512,
                                blank=True,
                                null=True,
                                help_text='Address line 2 to mail check to.')
    city = models.CharField(max_length=128,
                            help_text='The city portion of the address to mail check to.')
    state = USStateField(help_text='The state to mail check to.')
    zipcode = models.CharField(max_length=10,
                               help_text='The zipcode that the check should be mailed to.')

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

#     def save(self):
#         """
#         """
#         name = self.name.lower()
#         if name.starswith('the'):


class Website(models.Model):
    artist = models.ForeignKey(Artist)
    url = models.URLField()

class Photo(models.Model):
    artist = models.ForeignKey(Artist)
    image = models.ImageField(upload_to=upload_to)
    caption = models.CharField(max_length=256, blank=True, null=True)

    thumbnail = models.ImageField(upload_to=upload_to)

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s - %s" % (self.artist, self.image, self.caption)

    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        THUMBNAIL_WIDTH = 300

        image = Image.open(self.photo.image)

        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        # Compute thumbnail height
        wpercent = (basewidth/float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))

        image.thumbnail((THUMBNAIL_WIDTH, hsize), Image.ANTIALIAS)

        temp_handle = StringIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                 temp_handle.read(), content_type='image/png')
        self.thumbnail.save(suf.name+'_thumbnail.png', suf, save=False)

        super(Photo, self).save()

class Video(models.Model):
    artist = models.ForeignKey(Artist)
    video = models.FileField(upload_to=upload_to)
    caption = models.CharField(max_length=512)

    uploaded_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.caption

