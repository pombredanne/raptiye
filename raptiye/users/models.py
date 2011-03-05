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
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    """
    Stores additional information about the users..
    
    """
    
    user = models.OneToOneField(User, related_name='profile', verbose_name=_(u"User"))
    avatar = models.URLField(_(u"Avatar"), default=settings.DEFAULT_AVATAR)
    web_site = models.URLField(_(u"Web Site"), blank=True)
    comments_count = models.PositiveIntegerField(_(u"Comments Count"), default=0, editable=False)
    subscribed_entries = models.ManyToManyField("blog.Entry", related_name="subscribed_users", 
        verbose_name=_(u"Subscribed Entries"), null=True, db_table="subscribed_entries_per_profile")
    last_modified = models.DateTimeField(_(u"Last Modified Date"), auto_now=True)
    
    def __unicode__(self):
        return "User Profile of %s" % self.user
    
    class Meta:
        get_latest_by = "last_modified"
        ordering = ["-last_modified"]
        verbose_name = _(u"User Profile")
        verbose_name_plural = _(u"User Profiles")