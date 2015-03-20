# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_type',
            field=models.CharField(default=b'GENERIC', max_length=20, verbose_name=b'Group Type', choices=[(b'ACTIVE DIRECTORY', b'Active Directory'), (b'SOCIAL GROUP', b'Social Group'), (b'PROJECT', b'Project'), (b'WORKING GROUP', b'Working Group'), (b'TEAM', b'Team'), (b'GENERIC', b'Generic Group'), (b'ORGANISATION', b'Organisation'), (b'DISTRIBUTION LIST', b'Distribution List')]),
            preserve_default=True,
        ),
    ]
