# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifier',
            name='identifiertype',
            field=models.CharField(default=b'EMAIL', max_length=10, verbose_name=b'Identifier Type', choices=[(b'EMAIL', b'Email Address'), (b'SKYPE', b'Skype ID'), (b'IPADD', b'IP Address'), (b'UNAME', b'Username'), (b'TWITTER', b'Twitter ID')]),
            preserve_default=True,
        ),
    ]
