# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FlatPage'
        db.create_table('flatpages_flatpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('registration_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('template_name', self.gf('django.db.models.fields.CharField')(default='default.html', max_length=200, null=True, blank=True)),
            ('show_on_homepage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tags', self.gf('tagging.fields.TagField')(default='', null=True)),
        ))
        db.send_create_signal('flatpages', ['FlatPage'])

        # Adding M2M table for field sites on 'FlatPage'
        db.create_table('sites_per_flatpage', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flatpage', models.ForeignKey(orm['flatpages.flatpage'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('sites_per_flatpage', ['flatpage_id', 'site_id'])


    def backwards(self, orm):
        
        # Deleting model 'FlatPage'
        db.delete_table('flatpages_flatpage')

        # Removing M2M table for field sites on 'FlatPage'
        db.delete_table('sites_per_flatpage')


    models = {
        'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
