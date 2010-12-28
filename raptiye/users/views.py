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

from django.core.urlresolvers import reverse

from profiles.views import edit_profile as profiles_edit_profile

from raptiye.users.forms import ProfileForm

def edit_profile(request):
    """
    Wrapper function to django-profiles' edit_profile method for
    overriding success_url argument.
    
    """
    
    return profiles_edit_profile(request, form_class=ProfileForm,
        success_url=reverse("users:profiles_profile_detail", kwargs={
            "username": request.user.username
        }))