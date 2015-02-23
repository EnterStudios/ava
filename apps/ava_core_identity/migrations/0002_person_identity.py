# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='identity',
            field=models.ManyToManyField(to='ava_core_identity.Identity'),
            preserve_default=True,
        ),
    ]
