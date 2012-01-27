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

from forms import EntryForm
from models import *


__all__ = (
    'EntryAdmin',
    'LinkAdmin'
)


class EntryAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    date_hierarchy = "datetime"
    fieldsets = (
        (None, {
            "fields": ("title", "datetime", "content", "tags", "sites",
                ("comments_enabled", "sticky", "published"), "slug"),
        }),
        (_(u"Advanced Options"), {
            "classes": ("collapse",),
            "fields": ("template_name",)
        }),
    )
    form = EntryForm
    list_display = ("title", "datetime", "get_sites", "sticky", "published")
    list_filter = ("published", "sticky", "sites")
    list_per_page = settings.ADMIN_LIST_PER_PAGE
    ordering = ("-datetime", "title")
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True
    search_fields = ("title", "content")

    class Media:
        js = [
            '%s/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%s/js/tinymce_setup.js' % settings.STATIC_URL
        ]


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'window')
    list_filter = ('window',)
    search_fields = ['title', 'description']
    save_on_top = True

admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)
