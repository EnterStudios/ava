# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test', '0003_auto_20150327_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.TextField(max_length=500, verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Name'),
            preserve_default=True,
        ),
    ]
