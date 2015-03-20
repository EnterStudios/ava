# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test', '0001_squashed_0004_auto_20150320_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='via',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='host',
            field=models.CharField(max_length=260),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='ipaddress',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='method',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
