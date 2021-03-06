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

# nice or_ interface instead of a | b - amazing.. :)
import operator

from django.conf import settings
from django.db.models import Q

from models import Entry


__all__ = (
    "is_app_installed",
    "get_latest_entries",
    "search_against_entries"
)


def is_app_installed(app):
    if app in settings.INSTALLED_APPS:
        return True
    return False


def get_latest_entries(include_stickies=True):
    if include_stickies:
        return Entry.objects.filter(published=True)

    return Entry.objects.filter(published=True).exclude(sticky=True)


def search_against_entries(keywords):
    """
    Searches against the fields title, content and tags
    of each blog entry and returns the OR'ed list..

    """

    # FIXME: use a fts engine

    keyword_list = keywords.split(" ")
    q_list = []

    # creating a list of Q objects
    for keyword in keyword_list:
        q_list.append(Q(title__icontains=keyword) | Q(content__icontains=keyword))

        # creating an OR'ed Q from the list
        final_q = reduce(operator.or_, q_list)

        return get_latest_entries().filter(final_q).distinct()
