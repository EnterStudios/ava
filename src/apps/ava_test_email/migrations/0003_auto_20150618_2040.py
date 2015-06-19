# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_email', '0002_emailtestresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtest',
            name='fromaddr',
            field=models.EmailField(max_length=254),
        ),
    ]
