# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtype',
            name='icon',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testtype',
            name='url',
            field=models.TextField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timingtype',
            name='icon',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
