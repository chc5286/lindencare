# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Script'
        db.create_table(u'prescriptions_script', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opus_key', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('script_number', self.gf('django.db.models.fields.IntegerField')()),
            ('refill_number', self.gf('django.db.models.fields.IntegerField')()),
            ('date_of_service', self.gf('django.db.models.fields.DateField')()),
            ('deleted_date', self.gf('django.db.models.fields.DateField')()),
            ('drug_ndc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drugcompanies.DrugNDC'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
            ('commission_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salesreps.CommissionTag'])),
            ('acquisition_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Doctor'])),
            ('third_party_script', self.gf('django.db.models.fields.IntegerField')()),
            ('is_filled_by_robot', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_cash_posting_date', self.gf('django.db.models.fields.DateField')()),
            ('is_non_processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'prescriptions', ['Script'])

        # Adding model 'ScriptTransaction'
        db.create_table(u'prescriptions_scripttransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opus_key', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('opus_table', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('transaction_date', self.gf('django.db.models.fields.DateField')()),
            ('insuror', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insurance.Insuror'])),
            ('payor_order', self.gf('django.db.models.fields.IntegerField')()),
            ('is_non_processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted_date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'prescriptions', ['ScriptTransaction'])


    def backwards(self, orm):
        # Deleting model 'Script'
        db.delete_table(u'prescriptions_script')

        # Deleting model 'ScriptTransaction'
        db.delete_table(u'prescriptions_scripttransaction')


    models = {
        u'drugcompanies.division': {
            'Meta': {'object_name': 'Division'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drugcompanies.DrugCompany']"}),
            'drug': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['drugcompanies.Drug']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'drugcompanies.drug': {
            'Meta': {'object_name': 'Drug'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_brand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'drugcompanies.drugcompany': {
            'Meta': {'object_name': 'DrugCompany'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'drugcompanies.drugndc': {
            'Meta': {'object_name': 'DrugNDC'},
            'drug': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drugcompanies.Drug']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ndc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'opus_key': ('django.db.models.fields.IntegerField', [], {'default': '3', 'null': 'True', 'blank': 'True'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'strength_units': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'drugcompanies.drugrep': {
            'Meta': {'object_name': 'DrugRep'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drugcompanies.Manager']"}),
            'regions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'drugcompanies.manager': {
            'Meta': {'object_name': 'Manager'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drugcompanies.Division']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'territory': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
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
        u'practices.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'practices.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'commission_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesreps.CommissionTag']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'opus_key': ('django.db.models.fields.IntegerField', [], {'default': '1001', 'null': 'True', 'blank': 'True'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Practice']"})
        },
        u'practices.multipractice': {
            'Meta': {'object_name': 'MultiPractice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'practices.practice': {
            'Meta': {'object_name': 'Practice'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['practices.Category']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'drug_rep': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['drugcompanies.DrugRep']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideal_visits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'multi_practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.MultiPractice']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'next_visit': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'potential': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'sub_region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['regions.SubRegion']", 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'prescriptions.script': {
            'Meta': {'object_name': 'Script'},
            'acquisition_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'commission_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['salesreps.CommissionTag']"}),
            'date_of_service': ('django.db.models.fields.DateField', [], {}),
            'deleted_date': ('django.db.models.fields.DateField', [], {}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Doctor']"}),
            'drug_ndc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drugcompanies.DrugNDC']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_filled_by_robot': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_non_processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_cash_posting_date': ('django.db.models.fields.DateField', [], {}),
            'opus_key': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.Patient']"}),
            'refill_number': ('django.db.models.fields.IntegerField', [], {}),
            'script_number': ('django.db.models.fields.IntegerField', [], {}),
            'third_party_script': ('django.db.models.fields.IntegerField', [], {})
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
        },
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
        },
        u'salesreps.commissiontag': {
            'Meta': {'object_name': 'CommissionTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'})
        }
    }

    complete_apps = ['prescriptions']