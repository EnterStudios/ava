# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0004_auto_20150715_0116'),
        ('import_google', '0005_auto_20150715_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='identity',
        ),
        migrations.AddField(
            model_name='googledirectoryuser',
            name='identity',
            field=models.ForeignKey(default=1, to='core_identity.Identity'),
            preserve_default=False,
        ),
    ]
