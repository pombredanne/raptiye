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

from profiles.utils import get_profile_model

__all__ = ("ProfileForm",)

class ProfileForm(forms.Form):
    first_name = forms.CharField(label=_("first name"), max_length=30, required=False)
    last_name = forms.CharField(label=_("last name"), max_length=30, required=False)
    email = forms.EmailField(label=_("e-mail address"))
    web_site = forms.URLField(label=_("web site"), required=False, verify_exists=True)
    
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", get_profile_model())
        super(ProfileForm, self).__init__(*args, **kwargs)
    
    def save(self):
        user = self.instance.user
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save()
        self.instance.web_site = self.cleaned_data["web_site"]
        self.instance.save()
        return self.instance