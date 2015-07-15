# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0006_identity_identity_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identity',
            name='groups',
        ),
    ]
