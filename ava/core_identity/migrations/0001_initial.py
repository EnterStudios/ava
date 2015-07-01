# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('core_group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=100)),
                ('identifier_type', models.CharField(max_length=10, choices=[('EMAIL', 'Email Address'), ('SKYPE', 'Skype ID'), ('IPADD', 'IP Address'), ('UNAME', 'Username'), ('TWITTER', 'Twitter ID')], verbose_name='Identifier Type', default='EMAIL')),
            ],
            options={
                'ordering': ['identifier', 'identifier_type'],
            },
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('groups', models.ManyToManyField(blank=True, related_name='identities', null=True, to='core_group.Group')),
            ],
            options={
                'verbose_name_plural': 'identities',
                'verbose_name': 'identity',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('surname', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('identity', models.ManyToManyField(blank=True, to='core_identity.Identity')),
            ],
            options={
                'verbose_name_plural': 'people',
                'verbose_name': 'person',
                'ordering': ['surname', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='identifier',
            name='identity',
            field=models.ForeignKey(related_name='identifiers', to='core_identity.Identity'),
        ),
        migrations.AlterUniqueTogether(
            name='identifier',
            unique_together=set([('identifier', 'identifier_type', 'identity')]),
        ),
    ]
