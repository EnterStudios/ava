# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0002_auto_20150702_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], max_length=75),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], max_length=75),
        ),
    ]
