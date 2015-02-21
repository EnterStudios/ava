# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ExtendedProfile.person'
        db.alter_column(u'ava_core_people_extendedprofile', 'person_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ava_core_people.Person'], unique=True))
        # Adding unique constraint on 'ExtendedProfile', fields ['person']
        db.create_unique(u'ava_core_people_extendedprofile', ['person_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ExtendedProfile', fields ['person']
        db.delete_unique(u'ava_core_people_extendedprofile', ['person_id'])


        # Changing field 'ExtendedProfile.person'
        db.alter_column(u'ava_core_people_extendedprofile', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ava_core_people.Person']))

    models = {
        u'ava_core_people.extendedprofile': {
            'Meta': {'object_name': 'ExtendedProfile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ava_core_people.Person']", 'unique': 'True'})
        },
        u'ava_core_people.identifier': {
            'Meta': {'unique_together': "(('identifier', 'identifiertype', 'person'),)", 'object_name': 'Identifier'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'identifiertype': ('django.db.models.fields.CharField', [], {'default': "'EMAIL'", 'max_length': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ava_core_people.Person']"})
        },
        u'ava_core_people.person': {
            'Meta': {'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['ava_core_people']