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

from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from django.views.generic.simple import direct_to_template

from raptiye.blog.functions import is_app_installed

# TODO: migrate the code to class based generic views, functionals are deprecated!

urlpatterns = patterns('',
    url(r'^reset/password/being/confirmed/$', direct_to_template,
        {'template': 'password_reset_being_confirmed.html'}, name='password_reset_being_confirmed'),
    url(r'^reset/password/complete/$', direct_to_template,
        {'template': 'password_reset_complete.html'}, name='password_reset_complete'),
)

# builtin views with custom parameters
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {
        'template_name': 'login.html'
    }, name='login'),
    url(r'^logout/$', 'logout', {
        'template_name': 'logout.html'
    }, name='logout'),
    url(r'^reset/password/$', 'password_reset', {
        'template_name': 'password_reset_form.html',
        'email_template_name': 'password_reset_email.html',
        'post_reset_redirect': lazy(reverse, str)('users:password_reset_being_confirmed')
    }, name='password_reset'),
    url(r'^reset/password/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', {
        'template_name': 'password_reset_confirm.html',
        'post_reset_redirect': lazy(reverse, str)('users:password_reset_complete')
    }, name='password_reset_confirm'),
    url(r'^change/password/$', 'password_change', {
        'template_name': 'password_change_form.html',
        'post_change_redirect': lazy(reverse, str)('users:password_change_done')
    }, name='password_change'),
    url(r'^change/password/done/$', 'password_change_done', {
        'template_name': 'password_change_done.html'
    }, name='password_change_done')
)

if is_app_installed("registration"):
    urlpatterns += patterns('registration.views',
        url(r'^activate/complete/$', direct_to_template, {
            'template': 'registration/activation_complete.html'
        }, name='registration_activation_complete'),
        # Activation keys get matched by \w+ instead of the more specific
        # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
        # that way it can return a sensible "invalid key" message instead of a
        # confusing 404.
        url(r'^activate/(?P<activation_key>\w+)/$', 'activate', {
            'backend': 'registration.backends.default.DefaultBackend',
            'success_url': lazy(reverse, str)('users:registration_activation_complete')
        }, name='activate'),
        url(r'^register/$', 'register', {
            'backend': 'registration.backends.default.DefaultBackend',
            'success_url': lazy(reverse, str)('users:registration_complete')
        }, name='registration'),
        url(r'^register/complete/$', direct_to_template, {
            'template': 'registration/registration_complete.html'
        }, name='registration_complete')
    )

if is_app_installed("profiles"):
    urlpatterns += patterns('',
        url(r'^edit/$', 'raptiye.users.views.edit_profile', name='profiles_edit_profile'),
        url(r'^(?P<username>\w+)/$', 'profiles.views.profile_detail', name='profiles_profile_detail'),
    )