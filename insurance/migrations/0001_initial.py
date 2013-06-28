# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payor'
        db.create_table(u'insurance_payor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'insurance', ['Payor'])

        # Adding model 'BinNumber'
        db.create_table(u'insurance_binnumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bin_number', self.gf('django.db.models.fields.IntegerField')()),
            ('payor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insurance.Payor'], null=True, blank=True)),
        ))
        db.send_create_signal(u'insurance', ['BinNumber'])

        # Adding model 'Insuror'
        db.create_table(u'insurance_insuror', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carrier_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('plan_code', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('bin_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insurance.BinNumber'], null=True, blank=True)),
        ))
        db.send_create_signal(u'insurance', ['Insuror'])


    def backwards(self, orm):
        # Deleting model 'Payor'
        db.delete_table(u'insurance_payor')

        # Deleting model 'BinNumber'
        db.delete_table(u'insurance_binnumber')

        # Deleting model 'Insuror'
        db.delete_table(u'insurance_insuror')


    models = {
        u'insurance.binnumber': {
            'Meta': {'object_name': 'BinNumber'},
            'bin_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insurance.Payor']", 'null': 'True', 'blank': 'True'})
        },
        u'insurance.insuror': {
            'Meta': {'object_name': 'Insuror'},
            'bin_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insurance.BinNumber']", 'null': 'True', 'blank': 'True'}),
            'carrier_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'insurance.payor': {
            'Meta': {'object_name': 'Payor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['insurance']