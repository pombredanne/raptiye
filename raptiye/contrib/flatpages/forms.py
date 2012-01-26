# coding: utf-8
#
# raptiye
# Copyright (C) 2009  Alper Kanat <alperkanat@raptiye.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from django import forms
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _

from tagging.forms import TagField

from raptiye.blog.models import Entry
from raptiye.blog.widgets import *

from models import FlatPage


__all__ = ("FlatPageForm",)


class FlatPageForm(forms.ModelForm):
    tags = TagField(widget=AutoCompleteTagInput(model=Entry), required=False)
    url = forms.RegexField(label=_(u"URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text=_(u"Example: '/about/contact/'. Make sure to have leading and trailing slashes."),
        error_message=_(u"This value must contain only letters, numbers, underscores, dashes or slashes."))

    def clean_url(self):
        """
        Checks if url has trailing slash and raises
        ValidationError if not..

        """

        data = self.cleaned_data["url"]

        if data[-1] != "/":
            raise ValidationError(_(u"You should add a trailing slash at the end of the url."))

        return data

    class Meta:
        model = FlatPage
