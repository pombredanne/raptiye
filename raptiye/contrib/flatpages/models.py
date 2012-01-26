# coding: utf-8

from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from tagging.fields import TagField


__all__ = ("FlatPage",)


class FlatPage(models.Model):
    url = models.CharField(_(u'URL'), max_length=100, db_index=True)
    title = models.CharField(_(u'Title'), max_length=200)
    content = models.TextField(_(u'Content'), blank=True)
    # TODO: implement comments for flatpages
    enable_comments = models.BooleanField(_(u'Enable Comments'))
    registration_required = models.BooleanField(_(u'Registration required'),
        help_text=_(u"If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site, related_name="flatpages", verbose_name=_(u"Sites"),
        help_text=_(u"Required"), db_table="sites_per_flatpage")
    template_name = models.CharField(_(u"Template Name"), help_text=_(u"Required."),
        default="default.html", null=True, blank=True, max_length=200)
    show_on_homepage = models.BooleanField(_(u"Show on HomePage"), default=False)
    tags = TagField(_(u"Tags"), help_text=_(u"Seperated by commas"), null=True, blank=True)
    objects = CurrentSiteManager()

    def get_sites(self):
        return "<br>".join([
            "<a href='http://%s' target='_blank'>%s</a>" % (
                s.domain,
                s.name
            ) for s in self.sites.all()])

    get_sites.short_description = _(u"Published At")
    get_sites.allow_tags = True

    class Meta:
        ordering = ('url',)
        verbose_name = _(u'Flat Page')
        verbose_name_plural = _(u'Flat Pages')

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)
