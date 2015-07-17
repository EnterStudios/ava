# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oauth2client.django_orm
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.django_orm.CredentialsField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleConfiguration',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('domain', models.CharField(unique=True, verbose_name='Primary Domain', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoogleDirectoryGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=300)),
                ('google_id', models.CharField(unique=True, max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('admin_created', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('etag', models.CharField(max_length=300)),
                ('google_configuration', models.ForeignKey(to='import_google.GoogleConfiguration')),
            ],
            options={
                'ordering': ['name', 'google_id'],
            },
        ),
        migrations.CreateModel(
            name='GoogleDirectoryUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dn', models.CharField(max_length=300)),
                ('isDelegatedAdmin', models.BooleanField()),
                ('suspended', models.BooleanField()),
                ('google_id', models.CharField(max_length=300)),
                ('deletion_time', models.CharField(max_length=300)),
                ('suspension_reason', models.CharField(max_length=300)),
                ('is_admin', models.BooleanField()),
                ('etag', models.CharField(max_length=300)),
                ('last_login_time', models.CharField(max_length=300)),
                ('org_unit_path', models.CharField(max_length=300)),
                ('external_ids', models.CharField(max_length=300)),
                ('is_mailbox_setup', models.BooleanField()),
                ('password', models.CharField(max_length=300)),
                ('emails', models.CharField(max_length=300)),
                ('organizations', models.CharField(max_length=300)),
                ('primary_email', models.EmailField(max_length=254)),
                ('hash_function', models.CharField(max_length=300)),
                ('creation_time', models.CharField(max_length=300)),
                ('websites', models.CharField(max_length=300)),
                ('google_configuration', models.ForeignKey(to='import_google.GoogleConfiguration')),
                ('groups', models.ManyToManyField(related_name='users', to='import_google.GoogleDirectoryGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
