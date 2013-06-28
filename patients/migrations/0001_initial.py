# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'patients_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_inactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('opus_key', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('commission_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salesreps.CommissionTag'], null=True, blank=True)),
        ))
        db.send_create_signal(u'patients', ['Patient'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'patients_patient')


    models = {
        u'patients.patient': {
            'Meta': {'object_name': 'Patient'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'commission_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesreps.CommissionTag']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'opus_key': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'salesreps.commissiontag': {
            'Meta': {'object_name': 'CommissionTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'})
        }
    }

    complete_apps = ['patients']