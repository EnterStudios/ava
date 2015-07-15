# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_group', '0004_remove_group_identity'),
        ('core_identity', '0007_remove_identity_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='groups',
            field=models.ManyToManyField(blank=True, to='core_group.Group', related_name='identities'),
        ),
    ]
