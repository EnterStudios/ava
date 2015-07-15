# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_type',
            field=models.CharField(max_length=20, default='GENERIC', choices=[('ACTIVE DIRECTORY', 'Active Directory'), ('SOCIAL GROUP', 'Social Group'), ('PROJECT', 'Project'), ('WORKING GROUP', 'Working Group'), ('TEAM', 'Team'), ('GENERIC', 'Generic Group'), ('ORGANISATION', 'Organisation'), ('DISTRIBUTION LIST', 'Distribution List'), ('GOOGLE APPS', 'Google Apps Group')], verbose_name='Group Type'),
        ),
    ]
