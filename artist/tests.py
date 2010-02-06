# Brandon Edens
# 2010-01-21
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.contrib.auth.models import User
from django.test import TestCase

from jukebox.artist.models import Artist


###############################################################################
## Classes
###############################################################################

class ArtistTest(TestCase):

    def setUp(self):
        """
        """
        self.user = User.objects.create(
            username='jdoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'jdoe@as220.org',
            password = 'jojasdf23',
            )
        self.artist = Artist(user = self.user,
                             name = 'The Edens Experience',
                             description = 'This is a test artist.',
                             email_address = 'brandon@as220.org',
                             telephone_number = '401-529-0760',
                             pay_to_the_order_of = 'Brandon Edens',
                             address1 = '115 Empire St.',
                             city = 'Providence',
                             state = 'RI',
                             zipcode = '02903'
                             )
        self.artist.save()

    def test_name_handling_the(self):
        """
        """
        self.artist.name = 'tHe Edens Experience'
        self.artist.save()
        # Test that name is stored correctly.
        self.assertEquals(self.artist.name, 'Edens Experience, tHe')
        # Test that name is printed correctly.
        self.assertEquals(self.artist.__unicode__(), 'tHe Edens Experience')

    def test_name_handling_almost_the(self):
        """
        """
        self.artist.name = 'Theo Edens Experience'
        self.artist.save()
        # Test that name is not modified.
        self.assertEquals(self.artist.name, 'Theo Edens Experience')
        # Test that not modified name is printed correctly.
        self.assertEquals(self.artist.__unicode__(), 'Theo Edens Experience')

    def test_absolute_url(self):
        """
        """
        self.assertEquals(self.artist.get_absolute_url(),
                          "/artist/detail/%d/" % self.artist.id)

