# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InteractionType'
        db.create_table(u'interactions_interactiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(max_length=50)),
        ))
        db.send_create_signal(u'interactions', ['InteractionType'])

        # Adding model 'Interaction'
        db.create_table(u'interactions_interaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interactions.InteractionType'], null=True, blank=True)),
            ('table', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('person_id', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=300)),
        ))
        db.send_create_signal(u'interactions', ['Interaction'])


    def backwards(self, orm):
        # Deleting model 'InteractionType'
        db.delete_table(u'interactions_interactiontype')

        # Deleting model 'Interaction'
        db.delete_table(u'interactions_interaction')


    models = {
        u'interactions.interaction': {
            'Meta': {'object_name': 'Interaction'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person_id': ('django.db.models.fields.IntegerField', [], {}),
            'table': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['interactions.InteractionType']", 'null': 'True', 'blank': 'True'})
        },
        u'interactions.interactiontype': {
            'Meta': {'object_name': 'InteractionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['interactions']