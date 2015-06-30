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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('group_type', models.CharField(choices=[('ACTIVE DIRECTORY', 'Active Directory'), ('SOCIAL GROUP', 'Social Group'), ('PROJECT', 'Project'), ('WORKING GROUP', 'Working Group'), ('TEAM', 'Team'), ('GENERIC', 'Generic Group'), ('ORGANISATION', 'Organisation'), ('DISTRIBUTION LIST', 'Distribution List')], max_length=20, default='GENERIC', verbose_name='Group Type')),
                ('parent', models.ForeignKey(null=True, blank=True, to='core_group.Group')),
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
