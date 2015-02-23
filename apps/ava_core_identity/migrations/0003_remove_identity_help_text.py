# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0002_person_identity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identity',
            name='help_text',
        ),
    ]
