# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_google', '0009_auto_20150715_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='identity',
        ),
    ]
