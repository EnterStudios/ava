# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_project', '0003_auto_20150608_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='enddate',
            field=models.DateField(null=True, verbose_name=b'End Date', blank=True),
            preserve_default=True,
        ),
    ]
