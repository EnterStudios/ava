# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_group', '0001_initial'),
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
                ('group', models.ForeignKey(blank=True, to='ava_core_group.Group', null=True)),
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
                ('groups', models.ManyToManyField(related_name='users', to='ava_import_ldap.ActiveDirectoryGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LDAPConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_dn', models.CharField(max_length=100, verbose_name=b'User')),
                ('user_pw', models.CharField(max_length=100, verbose_name=b'Password')),
                ('dump_dn', models.CharField(max_length=100, verbose_name=b'Domain')),
                ('server', models.CharField(max_length=100, verbose_name=b'Server')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='ldapconfiguration',
            unique_together=set([('server', 'user_dn')]),
        ),
        migrations.AddField(
            model_name='activedirectoryuser',
            name='ldap_configuration',
            field=models.ForeignKey(to='ava_import_ldap.LDAPConfiguration'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='activedirectoryuser',
            unique_together=set([('objectGUID', 'objectSid')]),
        ),
        migrations.AddField(
            model_name='activedirectorygroup',
            name='ldap_configuration',
            field=models.ForeignKey(to='ava_import_ldap.LDAPConfiguration'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='activedirectorygroup',
            unique_together=set([('objectGUID', 'objectSid')]),
        ),
    ]
