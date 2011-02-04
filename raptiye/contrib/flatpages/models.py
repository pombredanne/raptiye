#-*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from tagging.fields import TagField

class FlatPage(models.Model):
    url = models.CharField(_(u'URL'), max_length=100, db_index=True)
    title = models.CharField(_(u'Title'), max_length=200)
    content = models.TextField(_(u'Content'), blank=True)
    # TODO: implement comments for flatpages
    enable_comments = models.BooleanField(_(u'Enable Comments'))
    template_name = models.CharField(_(u'Template Name'), max_length=70, blank=True, default="default.html")
    registration_required = models.BooleanField(_(u'Registration required'), help_text=_(u"If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site)
    show_on_homepage = models.BooleanField(_(u"Show on HomePage"), default=False)
    tags = TagField(_(u"Tags"), help_text=_(u"Seperated by commas"), null=True, blank=True)
    
    class Meta:
        ordering = ('url',)
        verbose_name = _(u'Flat Page')
        verbose_name_plural = _(u'Flat Pages')
    
    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)
    
    def get_absolute_url(self):
        return self.url