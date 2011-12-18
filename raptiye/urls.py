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
from django.contrib import admin

from raptiye.blog.functions import is_app_installed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'raptiye.blog.views.index', name="index"),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('raptiye.blog.urls', namespace='blog', app_name='blog'))
)

if is_app_installed('rosetta'):
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
