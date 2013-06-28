# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DrugCompany'
        db.create_table(u'drugcompanies_drugcompany', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'drugcompanies', ['DrugCompany'])

        # Adding model 'Drug'
        db.create_table(u'drugcompanies_drug', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('is_brand', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'drugcompanies', ['Drug'])

        # Adding model 'DrugNDC'
        db.create_table(u'drugcompanies_drugndc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opus_key', self.gf('django.db.models.fields.IntegerField')(default=3, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('drug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drugcompanies.Drug'], null=True, blank=True)),
            ('ndc', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('strength', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('strength_units', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'drugcompanies', ['DrugNDC'])

        # Adding model 'Division'
        db.create_table(u'drugcompanies_division', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drugcompanies.DrugCompany'])),
        ))
        db.send_create_signal(u'drugcompanies', ['Division'])

        # Adding M2M table for field drug on 'Division'
        m2m_table_name = db.shorten_name(u'drugcompanies_division_drug')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('division', models.ForeignKey(orm[u'drugcompanies.division'], null=False)),
            ('drug', models.ForeignKey(orm[u'drugcompanies.drug'], null=False))
        ))
        db.create_unique(m2m_table_name, ['division_id', 'drug_id'])

        # Adding model 'Manager'
        db.create_table(u'drugcompanies_manager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_inactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('division', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drugcompanies.Division'])),
            ('territory', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'drugcompanies', ['Manager'])

        # Adding model 'DrugRep'
        db.create_table(u'drugcompanies_drugrep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_inactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['drugcompanies.Manager'])),
            ('regions', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'drugcompanies', ['DrugRep'])


    def backwards(self, orm):
        # Deleting model 'DrugCompany'
        db.delete_table(u'drugcompanies_drugcompany')

        # Deleting model 'Drug'
        db.delete_table(u'drugcompanies_drug')

        # Deleting model 'DrugNDC'
        db.delete_table(u'drugcompanies_drugndc')

        # Deleting model 'Division'
        db.delete_table(u'drugcompanies_division')

        # Removing M2M table for field drug on 'Division'
        db.delete_table(db.shorten_name(u'drugcompanies_division_drug'))

        # Deleting model 'Manager'
        db.delete_table(u'drugcompanies_manager')

        # Deleting model 'DrugRep'
        db.delete_table(u'drugcompanies_drugrep')


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
        }
    }

    complete_apps = ['drugcompanies']