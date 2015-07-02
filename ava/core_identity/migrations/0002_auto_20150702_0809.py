# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='groups',
            field=models.ManyToManyField(related_name='identities', blank=True, to='core_group.Group'),
        ),
    ]
