# Brandon Edens
# 2010-02-05
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

from django import forms
from django.forms.forms import BoundField
from django import template


###############################################################################
## Classes
###############################################################################

class ModelForm(forms.ModelForm):

    def output_via_template(self):
        "Helper function for fieldsting fields data from form."
        bound_fields = [BoundField(self, field, name) for name, field \
                        in self.fields.items()]
        c = template.Context(dict(form = self, bound_fields = bound_fields))
        t = template.loader.get_template('forms/form.html')
        return t.render(c)

    def __unicode__(self):
        return self.output_via_template()

