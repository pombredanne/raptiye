# coding: utf-8
# 
# raptiye
# Copyright (C) 2009  Alper KANAT <alperkanat@raptiye.org>
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
from django.utils.translation import ugettext_lazy as _

from raptiye.users.models import UserProfile

__all__ = ("ProfileForm",)

class ProfileForm(forms.Form):
    first_name = forms.CharField(label=_("first name"), max_length=30, required=False)
    last_name = forms.CharField(label=_("last name"), max_length=30, required=False)
    email = forms.EmailField(label=_("e-mail address"))
    web_site = forms.URLField(label=_("web site"), required=False, verify_exists=True)
    
    def __init__(self, *args, **kwargs):
        if kwargs.has_key("instance"):
            form_data = {}
            self.instance = kwargs.pop("instance")
            # filling form data from existing profile information
            form_data["first_name"] = self.instance.user.first_name
            form_data["last_name"] = self.instance.user.last_name
            form_data["email"] = self.instance.user.email
            form_data["web_site"] = self.instance.web_site
            # passing form data to the form instance
            kwargs["initial"] = form_data
        super(ProfileForm, self).__init__(*args, **kwargs)
    
    def save(self):
        self.instance.user.first_name = self.cleaned_data["first_name"]
        self.instance.user.last_name = self.cleaned_data["last_name"]
        self.instance.user.email = self.cleaned_data["email"]
        self.instance.user.save()
        self.instance.web_site = self.cleaned_data["web_site"]
        self.instance.save()
        return self.instance