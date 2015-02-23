# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtype',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='timingtype',
            name='help_text',
        ),
    ]
