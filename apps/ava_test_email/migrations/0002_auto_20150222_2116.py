# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_email', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailmessagetype',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='emailtesttype',
            name='help_text',
        ),
    ]
