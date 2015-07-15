# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_google', '0008_googledirectorygroup_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='googledirectoryuser',
            name='first_name',
            field=models.CharField(max_length=300, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='googledirectoryuser',
            name='surname',
            field=models.CharField(max_length=300, default=1),
            preserve_default=False,
        ),
    ]
