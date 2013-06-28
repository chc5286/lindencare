# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'tasks_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'tasks', ['Category'])

        # Adding model 'Task'
        db.create_table(u'tasks_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 26, 0, 0))),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('is_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_in_schedule', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('practice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['practices.Practice'], null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Category'], null=True, blank=True)),
            ('urgency', self.gf('django.db.models.fields.CharField')(default='low', max_length=200)),
            ('sales_rep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
        ))
        db.send_create_signal(u'tasks', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'tasks_category')

        # Deleting model 'Task'
        db.delete_table(u'tasks_task')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        u'tasks.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_in_schedule': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['practices.Practice']", 'null': 'True', 'blank': 'True'}),
            'sales_rep': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'task_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 26, 0, 0)'}),
            'urgency': ('django.db.models.fields.CharField', [], {'default': "'low'", 'max_length': '200'})
        }
    }

    complete_apps = ['tasks']