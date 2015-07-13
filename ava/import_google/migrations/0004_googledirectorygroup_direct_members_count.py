# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_google', '0003_auto_20150713_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='googledirectorygroup',
            name='direct_members_count',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
