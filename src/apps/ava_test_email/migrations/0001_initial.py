# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.ava_test.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0001_initial'),
        ('ava_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('message_html', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailTest',
            fields=[
                ('test_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ava_test.Test')),
                ('fromaddr', models.EmailField(max_length=75)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('html_body', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('ava_test.test',),
        ),
        migrations.CreateModel(
            name='EmailTestTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(default=apps.ava_test.helpers.generate_hex_token, unique=True, max_length=100)),
                ('emailtest', models.ForeignKey(related_name='targets', to='ava_test_email.EmailTest')),
                ('target', models.ForeignKey(to='ava_core_identity.Identifier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='emailtesttarget',
            unique_together=set([('emailtest', 'target', 'token')]),
        ),
    ]
