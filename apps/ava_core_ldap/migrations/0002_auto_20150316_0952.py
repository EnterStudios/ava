# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_ldap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activedirectorygroup',
            name='group',
            field=models.ForeignKey(blank=True, to='ava_core_group.Group', null=True),
            preserve_default=True,
        ),
    ]
