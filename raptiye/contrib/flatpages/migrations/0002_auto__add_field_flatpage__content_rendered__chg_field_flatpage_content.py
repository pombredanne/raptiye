# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FlatPage._content_rendered'
        db.add_column('flatpages_flatpage', '_content_rendered', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Changing field 'FlatPage.content'
        db.alter_column('flatpages_flatpage', 'content', self.gf('markitup.fields.MarkupField')(no_rendered_field=True))


    def backwards(self, orm):
        
        # Deleting field 'FlatPage._content_rendered'
        db.delete_column('flatpages_flatpage', '_content_rendered')

        # Changing field 'FlatPage.content'
        db.alter_column('flatpages_flatpage', 'content', self.gf('django.db.models.fields.TextField')())


    models = {
        'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'flatpages'", 'symmetrical': 'False', 'db_table': "'sites_per_flatpage'", 'to': "orm['sites.Site']"}),
            'tags': ('tagging.fields.TagField', [], {'default': "''", 'null': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'default': "'default.html'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatpages']
