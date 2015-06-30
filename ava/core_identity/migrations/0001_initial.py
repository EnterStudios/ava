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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=100)),
                ('identifiertype', models.CharField(choices=[('EMAIL', 'Email Address'), ('SKYPE', 'Skype ID'), ('IPADD', 'IP Address'), ('UNAME', 'Username'), ('TWITTER', 'Twitter ID')], max_length=10, default='EMAIL', verbose_name='Identifier Type')),
            ],
            options={
                'ordering': ['identifier', 'identifiertype'],
            },
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('description', models.TextField(verbose_name='Description', max_length=500)),
                ('groups', models.ManyToManyField(null=True, related_name='identities', to='core_group.Group', blank=True)),
            ],
            options={
                'verbose_name': 'identity',
                'ordering': ['name'],
                'verbose_name_plural': 'identities',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('surname', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('identity', models.ManyToManyField(blank=True, to='core_identity.Identity')),
            ],
            options={
                'verbose_name': 'person',
                'ordering': ['surname', 'firstname'],
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AddField(
            model_name='identifier',
            name='identity',
            field=models.ForeignKey(to='core_identity.Identity', related_name='identifiers'),
        ),
        migrations.AlterUniqueTogether(
            name='identifier',
            unique_together=set([('identifier', 'identifiertype', 'identity')]),
        ),
    ]
