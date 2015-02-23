# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_org', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveDirectoryGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cn', models.CharField(max_length=300)),
                ('distinguishedName', models.CharField(unique=True, max_length=300)),
                ('name', models.CharField(max_length=100)),
                ('objectCategory', models.CharField(max_length=300)),
                ('sAMAccountName', models.CharField(max_length=300)),
                ('objectGUID', models.CharField(max_length=300)),
                ('objectSid', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActiveDirectoryUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('memberOf', models.ManyToManyField(to='ava_core_ldap.ActiveDirectoryGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QueryParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_dn', models.CharField(max_length=100, verbose_name=b'User')),
                ('user_pw', models.CharField(max_length=100, verbose_name=b'Password')),
                ('dump_dn', models.CharField(max_length=100, verbose_name=b'Domain')),
                ('server', models.CharField(max_length=100, verbose_name=b'Server')),
                ('organisation', models.ForeignKey(to='ava_core_org.Organisation')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='queryparameters',
            unique_together=set([('user', 'server', 'user_dn')]),
        ),
        migrations.AddField(
            model_name='activedirectoryuser',
            name='queryParameters',
            field=models.ForeignKey(to='ava_core_ldap.QueryParameters'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activedirectoryuser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='activedirectoryuser',
            unique_together=set([('objectGUID', 'objectSid')]),
        ),
        migrations.AddField(
            model_name='activedirectorygroup',
            name='member',
            field=models.ManyToManyField(to='ava_core_ldap.ActiveDirectoryUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activedirectorygroup',
            name='queryParameters',
            field=models.ForeignKey(to='ava_core_ldap.QueryParameters'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activedirectorygroup',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='activedirectorygroup',
            unique_together=set([('objectGUID', 'objectSid')]),
        ),
    ]
