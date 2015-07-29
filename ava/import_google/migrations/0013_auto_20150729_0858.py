# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_google', '0012_auto_20150729_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googledirectorygroup',
            name='google_id',
            field=models.CharField(max_length=300),
        ),
    ]
