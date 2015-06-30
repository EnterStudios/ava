# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ava.test.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0001_initial'),
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('message_html', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTest',
            fields=[
                ('test_ptr', models.OneToOneField(serialize=False, to='test.Test', primary_key=True, parent_link=True, auto_created=True)),
                ('fromaddr', models.EmailField(verbose_name='Send From Email Address', max_length=254)),
                ('subject', models.CharField(verbose_name='Subject', max_length=200)),
                ('body', models.TextField(verbose_name='Message Body')),
                ('is_html', models.BooleanField(verbose_name='Send as HTML Email?', default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('test.test',),
        ),
        migrations.CreateModel(
            name='EmailTestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ipaddress', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=10)),
                ('host', models.CharField(max_length=260)),
                ('path', models.TextField(null=True, blank=True)),
                ('contentlength', models.CharField(max_length=10, blank=True, null=True)),
                ('contenttype', models.CharField(max_length=100, blank=True, null=True)),
                ('ua', models.TextField(null=True, blank=True)),
                ('referrer', models.TextField(null=True, blank=True)),
                ('via', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailTestTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=100, default=ava.test.helpers.generate_hex_token, unique=True)),
                ('emailtest', models.ForeignKey(to='test_email.EmailTest', related_name='targets')),
                ('target', models.ForeignKey(to='core_identity.Identifier')),
            ],
        ),
        migrations.AddField(
            model_name='emailtestresult',
            name='target',
            field=models.ForeignKey(to='test_email.EmailTestTarget', related_name='results'),
        ),
        migrations.AlterUniqueTogether(
            name='emailtesttarget',
            unique_together=set([('emailtest', 'target', 'token')]),
        ),
    ]
