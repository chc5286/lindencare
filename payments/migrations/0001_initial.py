# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Batch'
        db.create_table(u'payments_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('date_deposited', self.gf('django.db.models.fields.DateField')()),
            ('date_added', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'payments', ['Batch'])

        # Adding model 'Check'
        db.create_table(u'payments_check', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('check_number', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('payor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insurance.Payor'], null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('date_deposited', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('fee', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['payments.Batch'], null=True, blank=True)),
        ))
        db.send_create_signal(u'payments', ['Check'])

        # Adding model 'PaymentType'
        db.create_table(u'payments_paymenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'payments', ['PaymentType'])

        # Adding model 'PaymentTransaction'
        db.create_table(u'payments_paymenttransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('script_transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prescriptions.ScriptTransaction'])),
            ('check', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['payments.Check'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('payment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['payments.PaymentType'])),
            ('date_received', self.gf('django.db.models.fields.DateField')()),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'payments', ['PaymentTransaction'])


    def backwards(self, orm):
        # Deleting model 'Batch'
        db.delete_table(u'payments_batch')

        # Deleting model 'Check'
        db.delete_table(u'payments_check')

        # Deleting model 'PaymentType'
        db.delete_table(u'payments_paymenttype')

        # Deleting model 'PaymentTransaction'
        db.delete_table(u'payments_paymenttransaction')


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
        },
        u'payments.batch': {
            'Meta': {'object_name': 'Batch'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_added': ('django.db.models.fields.DateField', [], {}),
            'date_deposited': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'payments.check': {
            'Meta': {'object_name': 'Check'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payments.Batch']", 'null': 'True', 'blank': 'True'}),
            'check_number': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_deposited': ('django.db.models.fields.DateField', [], {}),
            'fee': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insurance.Payor']", 'null': 'True', 'blank': 'True'})
        },
        u'payments.paymenttransaction': {
            'Meta': {'object_name': 'PaymentTransaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'check': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payments.Check']"}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_received': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['payments.PaymentType']"}),
            'script_transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescriptions.ScriptTransaction']"})
        },
        u'payments.paymenttype': {
            'Meta': {'object_name': 'PaymentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'prescriptions.scripttransaction': {
            'Meta': {'object_name': 'ScriptTransaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insuror': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insurance.Insuror']"}),
            'is_non_processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'opus_key': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'opus_table': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'payor_order': ('django.db.models.fields.IntegerField', [], {}),
            'transaction_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['payments']