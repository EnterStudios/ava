# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0007_remove_identity_groups'),
        ('core_group', '0002_auto_20150715_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='identity',
            field=models.ManyToManyField(blank=True, to='core_identity.Identity'),
        ),
    ]
