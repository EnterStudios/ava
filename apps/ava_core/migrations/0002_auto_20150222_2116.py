# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalstatus',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='group',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='mode',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='module',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='role',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='teststatus',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='userstatus',
            name='help_text',
        ),
    ]
