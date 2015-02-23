# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_org', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='organisationsize',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='organisationunittype',
            name='help_text',
        ),
    ]
