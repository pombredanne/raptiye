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
import logging

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from raptiye.blog.functions import get_latest_entries
from raptiye.blog.models import Link
from raptiye.blog.webcal import WebCalendar


__all__ = (
    'calculate_age',
    'webcal',
    'paginator',
    'links',
    'get_from_settings'
)


log = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def calculate_age():
    return (date.today() - settings.BIRTH_DATE).days / 365


@register.inclusion_tag('webcal.html', takes_context=True)
def webcal(context):
    wc = WebCalendar(get_latest_entries(), locale=settings.LOCALE)

    if "day" in context:
        year = context["day"].year
        month = context["day"].month
        day = context["day"].day
    elif "month" in context:
        year = context["month"].year
        month = context["month"].month
        day = None
    elif "entry" in context:
        year = context["entry"].datetime.year
        month = context["entry"].datetime.month
        day = context["entry"].datetime.day
    else:
        today = date.today()
        year = today.year
        month = today.month
        day = today.day

    return {
        "html": mark_safe(wc.formatmonth(year, month, day))
    }


@register.inclusion_tag('pagination.html', takes_context=True)
def paginator(context, adjacent_pages=2):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """

    paginator = context.get('paginator')
    page = context.get('page_obj')
    page_numbers = range(max(1, page.number - adjacent_pages), min(paginator.num_pages, page.number + adjacent_pages) + 1)
    params = context["request"].GET.copy()

    log.debug('Page Number: %s', page.number)
    log.debug('Number of Pages: %s', paginator.num_pages)
    log.debug('Page Range: %s', paginator.page_range)
    log.debug('Calculated Page Range: %s', page_numbers)
    log.debug('Next Page: %s', page.next_page_number())
    log.debug('Previous Page: %s', page.previous_page_number())
    log.debug('Has Next Page: %s', page.has_next())
    log.debug('Has Previous Page: %s', page.has_previous())
    log.debug('Query String: %s', params.urlencode())

    if params.__contains__("page"):
        del(params["page"])

    return {
        'page': page.number,
        'pages': paginator.num_pages,
        'page_numbers': page_numbers,
        'next': page.next_page_number(),
        'previous': page.previous_page_number(),
        'has_next': page.has_next(),
        'has_previous': page.has_previous(),
        'show_first': 1 not in page_numbers,
        'show_last': paginator.num_pages not in page_numbers,
        'query_string': params.urlencode(),
    }


@register.inclusion_tag('links.html')
def links():
    return {'links': Link.objects.all()}


@register.simple_tag
def get_from_settings(key, default=None):
    return settings.__getattr__(key, default)
