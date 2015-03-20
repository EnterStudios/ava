# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_email', '0002_auto_20150309_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtest',
            name='html_body',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtest',
            name='body',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtest',
            name='subject',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
