# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_group', '0003_group_identity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='identity',
        ),
    ]
