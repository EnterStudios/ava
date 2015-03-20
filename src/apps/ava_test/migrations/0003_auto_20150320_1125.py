# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test', '0002_auto_20150309_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='ipaddress',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testresult',
            name='referrer',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='requestinfo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='token',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='ua',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
