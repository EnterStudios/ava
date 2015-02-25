# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'ava_core_people_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ava_core_people', ['Person'])

        # Adding model 'Identifier'
        db.create_table(u'ava_core_people_identifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('identifiertype', self.gf('django.db.models.fields.CharField')(default='EMAIL', max_length=5)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
        ))
        db.send_create_signal(u'ava_core_people', ['Identifier'])

        # Adding model 'ExtendedProfile'
        db.create_table(u'ava_core_people_extendedprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recordstatus', self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person'])),
        ))
        db.send_create_signal(u'ava_core_people', ['ExtendedProfile'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'ava_core_people_person')

        # Deleting model 'Identifier'
        db.delete_table(u'ava_core_people_identifier')

        # Deleting model 'ExtendedProfile'
        db.delete_table(u'ava_core_people_extendedprofile')


    models = {
        u'ava_core_people.extendedprofile': {
            'Meta': {'object_name': 'ExtendedProfile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        },
        u'ava_core_people.identifier': {
            'Meta': {'object_name': 'Identifier'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'identifiertype': ('django.db.models.fields.CharField', [], {'default': "'EMAIL'", 'max_length': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'})
        },
        u'ava_core_people.person': {
            'Meta': {'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'recordstatus': ('django.db.models.fields.CharField', [], {'default': "'ACT'", 'max_length': '3'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ava_core_people']