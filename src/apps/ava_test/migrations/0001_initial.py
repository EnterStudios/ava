# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('testtype', models.CharField(default=b'EMAIL', max_length=7, verbose_name=b'Test Type', choices=[(b'EMAIL', b'Email'), (b'TWITTER', b'Twitter')])),
                ('teststatus', models.CharField(default=b'NEW', max_length=10, verbose_name=b'Test Status', choices=[(b'NEW', b'New'), (b'COMPLETE', b'Complete'), (b'ERROR', b'An error occurred'), (b'SCHEDULED', b'Scheduled'), (b'RUNNING', b'In progress')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=100)),
                ('ipaddress', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=10)),
                ('host', models.CharField(max_length=260)),
                ('path', models.TextField(null=True, blank=True)),
                ('contentlength', models.CharField(max_length=10, null=True, blank=True)),
                ('contenttype', models.CharField(max_length=100, null=True, blank=True)),
                ('ua', models.TextField(null=True, blank=True)),
                ('referrer', models.TextField(null=True, blank=True)),
                ('via', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
