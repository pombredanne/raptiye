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

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from forms import FlatPageForm
from models import FlatPage


__all__ = (
    'FlatPageAdmin',
)


class FlatPageAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    form = FlatPageForm
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'content', 'tags', 'sites', 'show_on_homepage')
        }),
        (_('Advanced Options'), {
            'classes': ('collapse',),
            'fields': ('enable_comments', 'registration_required', 'template_name')
        }),
    )
    list_display = ('url', 'title', 'get_sites', 'tags', 'show_on_homepage')
    list_filter = ('sites', 'enable_comments', 'registration_required', 'show_on_homepage')
    search_fields = ('url', 'title')

    class Media:
        js = [
            '%s/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%s/js/tinymce_setup.js' % settings.STATIC_URL
        ]

admin.site.register(FlatPage, FlatPageAdmin)
