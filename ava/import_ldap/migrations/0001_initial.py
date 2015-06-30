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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cn', models.CharField(max_length=300)),
                ('distinguishedName', models.CharField(max_length=300, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('objectCategory', models.CharField(max_length=300)),
                ('sAMAccountName', models.CharField(max_length=300)),
                ('objectGUID', models.CharField(max_length=300)),
                ('objectSid', models.CharField(max_length=300)),
                ('group', models.ForeignKey(null=True, blank=True, to='core_group.Group')),
            ],
            options={
                'ordering': ['cn', 'distinguishedName'],
            },
        ),
        migrations.CreateModel(
            name='ActiveDirectoryUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dn', models.CharField(max_length=300)),
                ('accountExpires', models.CharField(max_length=300)),
                ('adminCount', models.CharField(max_length=300)),
                ('badPasswordTime', models.CharField(max_length=300)),
                ('badPwdCount', models.CharField(max_length=300)),
                ('cn', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('displayName', models.CharField(max_length=300)),
                ('distinguishedName', models.CharField(max_length=300)),
                ('isCriticalSystemObject', models.CharField(max_length=300)),
                ('lastLogoff', models.CharField(max_length=300)),
                ('lastLogon', models.CharField(max_length=300)),
                ('lastLogonTimestamp', models.CharField(max_length=300)),
                ('logonCount', models.CharField(max_length=300)),
                ('logonHours', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('objectGUID', models.CharField(max_length=300)),
                ('objectSid', models.CharField(max_length=300)),
                ('primaryGroupID', models.CharField(max_length=300)),
                ('pwdLastSet', models.CharField(max_length=300)),
                ('sAMAccountName', models.CharField(max_length=300)),
                ('sAMAccountType', models.CharField(max_length=300)),
                ('uSNChanged', models.CharField(max_length=300)),
                ('uSNCreated', models.CharField(max_length=300)),
                ('userAccountControl', models.CharField(max_length=300)),
                ('whenChanged', models.CharField(max_length=300)),
                ('whenCreated', models.CharField(max_length=300)),
                ('groups', models.ManyToManyField(to='import_ldap.ActiveDirectoryGroup', related_name='users')),
            ],
            options={
                'ordering': ['cn', 'distinguishedName'],
            },
        ),
        migrations.CreateModel(
            name='LDAPConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
            unique_together=set([('objectGUID', 'objectSid')]),
        ),
        migrations.AlterUniqueTogether(
            name='activedirectorygroup',
            unique_together=set([('objectGUID', 'objectSid')]),
        ),
    ]
