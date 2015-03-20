# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.ava_test.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_email', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtesttarget',
            name='emailtest',
            field=models.ForeignKey(related_name='targets', to='ava_test_email.EmailTest'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtesttarget',
            name='token',
            field=models.CharField(default=apps.ava_test.helpers.generate_hex_token, unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
