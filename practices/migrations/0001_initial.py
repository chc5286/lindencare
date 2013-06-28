# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MultiPractice'
        db.create_table(u'practices_multipractice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'practices', ['MultiPractice'])

        # Adding model 'Category'
        db.create_table(u'practices_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'practices', ['Category'])

        # Adding model 'Practice'
        db.create_table(u'practices_practice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('multi_practice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.MultiPractice'], null=True, blank=True)),
            ('ideal_visits', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('potential', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('is_inactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('next_visit', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sub_region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['regions.SubRegion'], null=True, blank=True)),
        ))
        db.send_create_signal(u'practices', ['Practice'])

        # Adding M2M table for field category on 'Practice'
        m2m_table_name = db.shorten_name(u'practices_practice_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('practice', models.ForeignKey(orm[u'practices.practice'], null=False)),
            ('category', models.ForeignKey(orm[u'practices.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['practice_id', 'category_id'])

        # Adding M2M table for field drug_rep on 'Practice'
        m2m_table_name = db.shorten_name(u'practices_practice_drug_rep')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('practice', models.ForeignKey(orm[u'practices.practice'], null=False)),
            ('drugrep', models.ForeignKey(orm[u'drugcompanies.drugrep'], null=False))
        ))
        db.create_unique(m2m_table_name, ['practice_id', 'drugrep_id'])

        # Adding model 'ContactType'
        db.create_table(u'practices_contacttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'practices', ['ContactType'])

        # Adding model 'Doctor'
        db.create_table(u'practices_doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_inactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('practice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Practice'])),
            ('opus_key', self.gf('django.db.models.fields.IntegerField')(default=1001, null=True, blank=True)),
            ('commission_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['salesreps.CommissionTag'], null=True)),
        ))
        db.send_create_signal(u'practices', ['Doctor'])

        # Adding model 'PracticeContact'
        db.create_table(u'practices_practicecontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_inactive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('practice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Practice'])),
            ('contact_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.ContactType'])),
        ))
        db.send_create_signal(u'practices', ['PracticeContact'])


    def backwards(self, orm):
        # Deleting model 'MultiPractice'
        db.delete_table(u'practices_multipractice')

        # Deleting model 'Category'
        db.delete_table(u'practices_category')

        # Deleting model 'Practice'
        db.delete_table(u'practices_practice')

        # Removing M2M table for field category on 'Practice'
        db.delete_table(db.shorten_name(u'practices_practice_category'))

        # Removing M2M table for field drug_rep on 'Practice'
        db.delete_table(db.shorten_name(u'practices_practice_drug_rep'))

        # Deleting model 'ContactType'
        db.delete_table(u'practices_contacttype')

        # Deleting model 'Doctor'
        db.delete_table(u'practices_doctor')

        # Deleting model 'PracticeContact'
        db.delete_table(u'practices_practicecontact')


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
        u'practices.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'practices.contacttype': {
            'Meta': {'object_name': 'ContactType'},
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
        u'practices.practicecontact': {
            'Meta': {'object_name': 'PracticeContact'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.ContactType']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Practice']"})
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

    complete_apps = ['practices']