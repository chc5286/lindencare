# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'regions_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'regions', ['Region'])

        # Adding model 'SubRegion'
        db.create_table(u'regions_subregion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['regions.Region'])),
        ))
        db.send_create_signal(u'regions', ['SubRegion'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'regions_region')

        # Deleting model 'SubRegion'
        db.delete_table(u'regions_subregion')


    models = {
        u'regions.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'regions.subregion': {
            'Meta': {'object_name': 'SubRegion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['regions.Region']"})
        }
    }

    complete_apps = ['regions']