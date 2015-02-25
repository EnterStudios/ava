# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Identifier.recordstatus'
        db.delete_column(u'ava_core_people_identifier', 'recordstatus')

        # Deleting field 'Person.recordstatus'
        db.delete_column(u'ava_core_people_person', 'recordstatus')

        # Deleting field 'ExtendedProfile.recordstatus'
        db.delete_column(u'ava_core_people_extendedprofile', 'recordstatus')


    def backwards(self, orm):
        # Adding field 'Identifier.recordstatus'
        db.add_column(u'ava_core_people_identifier', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'Person.recordstatus'
        db.add_column(u'ava_core_people_person', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)

        # Adding field 'ExtendedProfile.recordstatus'
        db.add_column(u'ava_core_people_extendedprofile', 'recordstatus',
                      self.gf('django.db.models.fields.CharField')(default='ACT', max_length=3),
                      keep_default=False)


    models = {
        u'ava_core_people.extendedprofile': {
            'Meta': {'object_name': 'ExtendedProfile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"})
        },
        u'ava_core_people.identifier': {
            'Meta': {'object_name': 'Identifier'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'identifiertype': ('django.db.models.fields.CharField', [], {'default': "'EMAIL'", 'max_length': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"})
        },
        u'ava_core_people.person': {
            'Meta': {'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ava_core_people']