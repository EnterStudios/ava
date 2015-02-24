# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=100)),
                ('identifiertype', models.CharField(default=b'EMAIL', max_length=7, verbose_name=b'Identifier Type', choices=[(b'EMAIL', b'Email Address'), (b'SKYPE', b'Skype ID'), (b'IPADD', b'IP Address'), (b'UNAME', b'Username'), (b'TWITTER', b'Twitter ID')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'identity',
                'verbose_name_plural': 'identities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('surname', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('identity', models.ManyToManyField(to='ava_core_identity.Identity')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='identifier',
            name='identity',
            field=models.ForeignKey(to='ava_core_identity.Identity'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='identifier',
            unique_together=set([('identifier', 'identifiertype', 'identity')]),
        ),
    ]
