# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveDirectoryGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cn', models.CharField(max_length=300)),
                ('distinguished_name', models.CharField(unique=True, max_length=300)),
                ('name', models.CharField(max_length=100)),
                ('object_category', models.CharField(max_length=300)),
                ('sam_account_name', models.CharField(max_length=300)),
                ('object_guid', models.CharField(max_length=300)),
                ('object_sid', models.CharField(max_length=300)),
                ('group', models.ForeignKey(to='core_group.Group', null=True, blank=True)),
            ],
            options={
                'ordering': ['cn', 'distinguished_name'],
            },
        ),
        migrations.CreateModel(
            name='ActiveDirectoryUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dn', models.CharField(max_length=300)),
                ('account_expires', models.CharField(max_length=300)),
                ('admin_count', models.IntegerField(null=True)),
                ('bad_password_time', models.CharField(max_length=300)),
                ('bad_pwd_count', models.IntegerField(null=True)),
                ('cn', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('display_name', models.CharField(max_length=300)),
                ('distinguished_name', models.CharField(max_length=300)),
                ('is_critical_system_object', models.CharField(max_length=300)),
                ('last_logoff', models.CharField(max_length=300)),
                ('last_logon', models.CharField(max_length=300)),
                ('last_logon_timestamp', models.CharField(max_length=300)),
                ('logon_count', models.IntegerField(null=True)),
                ('logon_hours', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('object_guid', models.CharField(max_length=300)),
                ('object_sid', models.CharField(max_length=300)),
                ('primary_group_id', models.CharField(max_length=300)),
                ('pwd_last_set', models.CharField(max_length=300)),
                ('sam_account_name', models.CharField(max_length=300)),
                ('sam_account_type', models.CharField(max_length=300)),
                ('usn_changed', models.CharField(max_length=300)),
                ('usn_created', models.CharField(max_length=300)),
                ('user_account_control', models.CharField(max_length=300)),
                ('when_changed', models.CharField(max_length=300)),
                ('when_created', models.CharField(max_length=300)),
                ('groups', models.ManyToManyField(to='import_ldap.ActiveDirectoryGroup', related_name='users')),
            ],
            options={
                'ordering': ['cn', 'distinguished_name'],
            },
        ),
        migrations.CreateModel(
            name='LDAPConfiguration',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_dn', models.CharField(verbose_name='User', max_length=100)),
                ('user_pw', models.CharField(verbose_name='Password', max_length=100)),
                ('dump_dn', models.CharField(verbose_name='Domain', max_length=100)),
                ('server', models.CharField(verbose_name='Server', max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ldapconfiguration',
            unique_together=set([('server', 'user_dn')]),
        ),
        migrations.AddField(
            model_name='activedirectoryuser',
            name='ldap_configuration',
            field=models.ForeignKey(to='import_ldap.LDAPConfiguration'),
        ),
        migrations.AddField(
            model_name='activedirectorygroup',
            name='ldap_configuration',
            field=models.ForeignKey(to='import_ldap.LDAPConfiguration'),
        ),
        migrations.AlterUniqueTogether(
            name='activedirectoryuser',
            unique_together=set([('object_guid', 'object_sid')]),
        ),
        migrations.AlterUniqueTogether(
            name='activedirectorygroup',
            unique_together=set([('object_guid', 'object_sid')]),
        ),
    ]
