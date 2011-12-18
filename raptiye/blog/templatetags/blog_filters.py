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

import HTMLParser

from django import template
from django.conf import settings

from raptiye.blog.functions import is_app_installed

register = template.Library()


@register.filter
def emotions(entry):
    if not settings.ENABLE_EMOTIONS:
        return entry

    icons = {
        ":)": "%simages/smiley/face-smile.png" % settings.STATIC_URL,
        ":|": "%simages/smiley/face-plain.png" % settings.STATIC_URL,
        ":(": "%simages/smiley/face-sad.png" % settings.STATIC_URL,
        ":D": "%simages/smiley/face-grin.png" % settings.STATIC_URL,
        ";-)": "%simages/smiley/face-wink.png" % settings.STATIC_URL,
    }

    for smiley, src in icons.iteritems():
        entry = entry.replace(smiley, " <img src='%s' align='absmiddle'> " % (src))

    return entry


@register.filter
def exceeds_limit(entry):
    if len(entry.split()) > 150:
        return True
    return False


@register.filter
def code_colorizer(entry):
    """
    Uses BeautifulSoup to find and parse the code in the entry
    that will be colorized and changes it according to the syntax
    specs using pygments.

    The HTML code should include the colorized code wrapped into a
    div which has language (e.g. python) as id and "code" as class
    attributes.

    Best part of using a filter is that we don't have to change the
    real post containing the code. The worst part is that we have to
    search for the code layer in each post.

    """

    if settings.COLORIZE_CODE:
        try:
            from BeautifulSoup import BeautifulSoup, Tag
            from pygments import highlight
            from pygments.lexers import get_lexer_by_name
            from pygments.formatters import HtmlFormatter
        except ImportError:
            return entry

        try:
            parser = BeautifulSoup(entry, convertEntities=BeautifulSoup.ALL_ENTITIES)
        except HTMLParser.HTMLParseError:
            return entry

        # searching for code blocks in the blog entry
        code_blocks = parser.findAll("div", attrs={"class": "code"})

        if len(code_blocks) > 0:
            for block in code_blocks:
                # if the code block's wrapper div doesn't have an id
                # attribute don't colorize the code
                if "id" in block.attrMap:
                    language = block.attrMap["id"]
                else:
                    continue

                # finding the exact place of the code
                layer = block.div if block.div else block
                # removing any html tags inside the code block
                [tag.extract() for tag in layer.findAll()]
                # getting the original code in the block
                code = "".join(layer.contents)
                # colorizing the code
                lexer = get_lexer_by_name(language)
                formatter = HtmlFormatter(linenos="table", style="tango", cssclass="code")
                colorized_code = Tag(parser, "div") if block.div else Tag(parser, "div", attrs=(("id", language), ("class", "code")))
                colorized_code.insert(0, highlight(code, lexer, formatter))
                layer.replaceWith(colorized_code)

            return parser.renderContents()

    return entry


@register.filter
def is_installed(app):
    return is_app_installed(app)
