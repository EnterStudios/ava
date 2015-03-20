# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'ava_test', '0001_initial'), (b'ava_test', '0002_auto_20150309_1434'), (b'ava_test', '0003_auto_20150320_1125'), (b'ava_test', '0004_auto_20150320_1150')]

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
                ('teststatus', models.CharField(default=b'NEW', max_length=10, verbose_name=b'Test Status', choices=[(b'NEW', b'New'), (b'COMPLETE', b'Complete'), (b'ERROR', b'An error occurred'), (b'SCHEDULED', b'Scheduled'), (b'RUNNING', b'In progress')])),
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
                ('ua', models.TextField(null=True, blank=True)),
                ('ipaddress', models.CharField(default=None, max_length=50)),
                ('referrer', models.TextField(null=True, blank=True)),
                ('contentlength', models.CharField(max_length=10, null=True, blank=True)),
                ('contenttype', models.CharField(max_length=100, null=True, blank=True)),
                ('host', models.CharField(default=None, max_length=260)),
                ('method', models.CharField(default=None, max_length=10)),
                ('path', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('url', models.TextField(max_length=50)),
                ('icon', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='test',
            name='testtype',
            field=models.ForeignKey(to='ava_test.TestType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='timingtype',
            field=models.ForeignKey(to='ava_test.TimingType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
