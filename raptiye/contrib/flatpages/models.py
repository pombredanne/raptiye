#-*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from tagging.fields import TagField

class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    # TODO: implement comments for flatpages
    enable_comments = models.BooleanField(_('enable comments'))
    template_name = models.CharField(_('template name'), max_length=70, blank=True, default="default.html")
    registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site)
    show_on_homepage = models.BooleanField(_("Show on HomePage"), default=False)
    tags = TagField(_(u"Tags"), help_text=_(u"Seperated by commas"), null=True, blank=True)
    
    class Meta:
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('url',)
    
    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)
    
    def get_absolute_url(self):
        return self.url