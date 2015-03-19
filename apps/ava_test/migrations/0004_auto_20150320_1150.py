# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test', '0003_auto_20150320_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='requestinfo',
        ),
        migrations.AddField(
            model_name='testresult',
            name='contentlength',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='contenttype',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='host',
            field=models.CharField(default=None, max_length=260),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testresult',
            name='method',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testresult',
            name='path',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
