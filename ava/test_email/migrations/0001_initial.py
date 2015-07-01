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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('message_html', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTest',
            fields=[
                ('test_ptr', models.OneToOneField(auto_created=True, serialize=False, to='test.Test', primary_key=True, parent_link=True)),
                ('fromaddr', models.EmailField(max_length=254, verbose_name='Send From Email Address')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ip_address', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=10)),
                ('host', models.CharField(max_length=260)),
                ('path', models.TextField(blank=True, null=True)),
                ('content_length', models.CharField(blank=True, max_length=10, null=True)),
                ('content_type', models.CharField(blank=True, max_length=100, null=True)),
                ('ua', models.TextField(blank=True, null=True)),
                ('referrer', models.TextField(blank=True, null=True)),
                ('via', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailTestTarget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(unique=True, max_length=100, default=ava.test.helpers.generate_hex_token)),
                ('emailtest', models.ForeignKey(related_name='targets', to='test_email.EmailTest')),
                ('target', models.ForeignKey(to='core_identity.Identifier')),
            ],
        ),
        migrations.AddField(
            model_name='emailtestresult',
            name='target',
            field=models.ForeignKey(related_name='results', to='test_email.EmailTestTarget'),
        ),
        migrations.AlterUniqueTogether(
            name='emailtesttarget',
            unique_together=set([('emailtest', 'target', 'token')]),
        ),
    ]
