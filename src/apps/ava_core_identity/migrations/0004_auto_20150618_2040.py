# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0003_auto_20150402_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='identifier',
            options={'ordering': ['identifier', 'identifiertype']},
        ),
    ]
