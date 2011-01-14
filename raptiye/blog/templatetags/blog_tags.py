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

from datetime import date

from django import template
from django.conf import settings

from raptiye.blog.functions import get_latest_entries
from raptiye.blog.models import Link
from raptiye.blog.webcal import WebCalendar

register = template.Library()

@register.simple_tag
def calculate_age():
    return (date.today() - settings.BIRTH_DATE).days/365

@register.simple_tag
def construct_calendar(year=date.today().year, month=date.today().month, day=date.today().day):
    wc = WebCalendar(get_latest_entries(), locale=settings.LOCALES["tr"])
    return wc.formatmonth(year, month, day)

@register.inclusion_tag('pagination.html', takes_context=True)
def paginator(context, adjacent_pages=2):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """

    page_numbers = range(max(1, context['page'] - adjacent_pages), min(context['pages'], context['page'] + adjacent_pages) + 1)

    params = context["request"].GET.copy()

    if params.__contains__("page"):
        del(params["page"])

    return {
        'page': context['page'],
        'pages': context['pages'],
        'page_numbers': page_numbers,
        'next': context['next'],
        'previous': context['previous'],
        'has_next': context['has_next'],
        'has_previous': context['has_previous'],
        'show_first': 1 not in page_numbers,
        'show_last': context['pages'] not in page_numbers,
        'query_string': params.urlencode(),
    }

@register.inclusion_tag('links.html')
def links():
    return {'links': Link.objects.all()}

@register.simple_tag
def project_name():
    return settings.PROJECT_NAME

@register.simple_tag
def version():
    return settings.VERSION

@register.simple_tag
def project_subtitle():
    return settings.PROJECT_SUBTITLE

@register.simple_tag
def rss_url():
    return settings.RSS_URL