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

from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic.dates import DayArchiveView, DateDetailView, MonthArchiveView
from django.views.generic.list import ListView

from feeds import *
from functions import get_latest_entries

urlpatterns = patterns('raptiye.blog.views',
    # main page of blog
    url(r'^$', ListView.as_view(**{
        'queryset': get_latest_entries(),
        'template_name': '%s/homepage.html' % settings.TEMPLATE_NAME,
        'paginate_by': settings.ENTRIES_PER_PAGE,
        'context_object_name': 'entries'
    }), name='index'),

    # archives for blogs..
    # url(r'^(?P<year>\d{4})/$', 'get_entries_for_year', name='entries_in_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', MonthArchiveView.as_view(**{
        'queryset': get_latest_entries(),
        'date_field': 'datetime',
        'month_format': '%m',
        'allow_empty': True,
        'context_object_name': "entries",
        'allow_future': True,
        'paginate_by': settings.ENTRIES_PER_PAGE,
        'template_name': '%s/entries_in_month.html' % settings.TEMPLATE_NAME,
    }), name='entries_in_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', DayArchiveView.as_view(**{
        'queryset': get_latest_entries(),
        'date_field': 'datetime',
        'month_format': '%m',
        'allow_empty': True,
        'context_object_name': "entries",
        'allow_future': True,
        'paginate_by': settings.ENTRIES_PER_PAGE,
        'template_name': '%s/entries_for_day.html' % settings.TEMPLATE_NAME,
    }), name='entries_on_date'),
    # an entry on a specific date
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[\w\d-]+)/$', DateDetailView.as_view(**{
        'queryset': get_latest_entries(),
        'date_field': 'datetime',
        'month_format': '%m',
        'context_object_name': "entry",
        'allow_future': True,
        'template_name': '%s/detail.html' % settings.TEMPLATE_NAME
    }), name='show_post'),

    # feeds
    url(r'^feeds/latest/$', RSSLatestEntries(), name="rss_entries_latest"),
    url(r'^feeds/(?P<tag>[^/]+)/$', RSSEntriesTaggedWith(), name="rss_entries_tagged_with"),

    # search against entries
    url(r'^search/$', 'search', name='search'),

    # tags
    url(r'^tags/(?P<tag>[^/]+)/$', 'entries_tagged_with', name='entries_tagged_with'),
)
