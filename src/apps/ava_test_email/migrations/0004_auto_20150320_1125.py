# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_email', '0003_auto_20150319_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='message_html',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='subject',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
