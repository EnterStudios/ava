# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('group_type', models.CharField(max_length=20, choices=[('ACTIVE DIRECTORY', 'Active Directory'), ('SOCIAL GROUP', 'Social Group'), ('PROJECT', 'Project'), ('WORKING GROUP', 'Working Group'), ('TEAM', 'Team'), ('GENERIC', 'Generic Group'), ('ORGANISATION', 'Organisation'), ('DISTRIBUTION LIST', 'Distribution List')], verbose_name='Group Type', default='GENERIC')),
                ('parent', models.ForeignKey(null=True, to='core_group.Group', blank=True)),
            ],
            options={
                'ordering': ['name', 'group_type'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('name', 'group_type')]),
        ),
    ]
