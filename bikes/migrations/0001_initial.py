# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Bike'
        db.create_table('bikes_bike', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('motto', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bikes', ['Bike'])

        # Adding model 'Image'
        db.create_table('bikes_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bike', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bike', to=orm['bikes.Bike'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('file', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('bikes', ['Image'])


    def backwards(self, orm):
        
        # Deleting model 'Bike'
        db.delete_table('bikes_bike')

        # Deleting model 'Image'
        db.delete_table('bikes_image')


    models = {
        'bikes.bike': {
            'Meta': {'object_name': 'Bike'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motto': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'bikes.image': {
            'Meta': {'object_name': 'Image'},
            'bike': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bike'", 'to': "orm['bikes.Bike']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bikes']
