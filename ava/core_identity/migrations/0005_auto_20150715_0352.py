# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0004_auto_20150715_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifier',
            name='identifier_type',
            field=models.CharField(max_length=10, verbose_name='Identifier Type', choices=[('EMAIL', 'Email Address'), ('SKYPE', 'Skype ID'), ('IPADD', 'IP Address'), ('UNAME', 'Username'), ('TWITTER', 'Twitter ID'), ('NAME', 'Other name')], default='EMAIL'),
        ),
    ]
