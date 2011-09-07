# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Image.created_date'
        db.add_column('bikes_image', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 9, 7), blank=True), keep_default=False)

        # Adding field 'Image.last_updated'
        db.add_column('bikes_image', 'last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, default=datetime.date(2011, 9, 7), blank=True), keep_default=False)

        # Adding field 'Bike.created_date'
        db.add_column('bikes_bike', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 9, 7), blank=True), keep_default=False)

        # Adding field 'Bike.last_updated'
        db.add_column('bikes_bike', 'last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, default=datetime.date(2011, 9, 7), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Image.created_date'
        db.delete_column('bikes_image', 'created_date')

        # Deleting field 'Image.last_updated'
        db.delete_column('bikes_image', 'last_updated')

        # Deleting field 'Bike.created_date'
        db.delete_column('bikes_bike', 'created_date')

        # Deleting field 'Bike.last_updated'
        db.delete_column('bikes_bike', 'last_updated')


    models = {
        'bikes.bike': {
            'Meta': {'object_name': 'Bike'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'motto': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'bikes.image': {
            'Meta': {'object_name': 'Image'},
            'bike': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bike'", 'to': "orm['bikes.Bike']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bikes']
