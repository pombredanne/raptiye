# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Entry'
        db.create_table('blog_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('sticky', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comments_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
            ('tags', self.gf('tagging.fields.TagField')(default='')),
            ('template_name', self.gf('django.db.models.fields.CharField')(default='homepage.html', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Entry'])

        # Adding M2M table for field sites on 'Entry'
        db.create_table('sites_per_entry', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['blog.entry'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('sites_per_entry', ['entry_id', 'site_id'])

        # Adding model 'Link'
        db.create_table('blog_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='50')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length='200', blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('window', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('blog', ['Link'])


    def backwards(self, orm):
        
        # Deleting model 'Entry'
        db.delete_table('blog_entry')

        # Removing M2M table for field sites on 'Entry'
        db.delete_table('sites_per_entry')

        # Deleting model 'Link'
        db.delete_table('blog_link')


    models = {
        'blog.entry': {
            'Meta': {'ordering': "['-datetime', 'title', 'content']", 'object_name': 'Entry'},
            'comments_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'entries'", 'symmetrical': 'False', 'db_table': "'sites_per_entry'", 'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tags': ('tagging.fields.TagField', [], {'default': "''"}),
            'template_name': ('django.db.models.fields.CharField', [], {'default': "'homepage.html'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'blog.link': {
            'Meta': {'ordering': "['title']", 'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'window': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']
