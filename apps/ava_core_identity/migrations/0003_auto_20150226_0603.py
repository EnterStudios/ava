# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0002_auto_20150225_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='identity',
            field=models.ManyToManyField(to='ava_core_identity.Identity', blank=True),
            preserve_default=True,
        ),
    ]
