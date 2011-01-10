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

import calendar

from django.core.urlresolvers import reverse

class WebCalendar(calendar.LocaleHTMLCalendar):
    def __init__(self, obj_list, queryField="datetime", cssClass="ulink", firstweekday=0, locale=None):
        super(WebCalendar, self).__init__(firstweekday, locale)
        self.obj_list = obj_list
        self.queryField = queryField
        self.cssClass = cssClass

    def haveObjForDate(self):
        filters = {
            "%s__year" % self.queryField: self.year,
            "%s__month" % self.queryField: self.month,
            "%s__day" % self.queryField: self.day
        }

        return self.obj_list.filter(**filters).exists()

    def formatmonth(self, year, month, selectedDay=None):
        self.year = year
        self.month = month
        self.selectedDay = selectedDay

        tableData = super(WebCalendar, self).formatmonth(year, month)

        return tableData

    def formatday(self, day, weekday):
        self.day = day

        if day != 0:
            cellCSS = "%s %s" % (
                self.cssclasses[weekday], "today"
            ) if self.day == self.selectedDay else self.cssclasses[weekday]

            cellValue = '<a href="%s" class="%s">%d</a>' % (
                reverse("blog:entries_on_date", args=[self.year, self.month, self.day]),
                self.cssClass,
                day
            ) if self.haveObjForDate() else "%d" % day

            return '<td class="%s">%s</td>' % (cellCSS, cellValue)

        return '<td class="noday">&nbsp;</td>'