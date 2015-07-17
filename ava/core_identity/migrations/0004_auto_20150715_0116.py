# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0003_auto_20150710_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='description',
            field=models.TextField(null=True, verbose_name='Description', blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='identity',
            name='name',
            field=models.CharField(null=True, verbose_name='Name', blank=True, max_length=100),
        ),
    ]
