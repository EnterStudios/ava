# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0005_auto_20150715_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='identity_type',
            field=models.CharField(max_length=10, choices=[('GROUP', 'Group'), ('PERSON', 'Person')], default='PERSON', verbose_name='Identity Type'),
        ),
    ]
