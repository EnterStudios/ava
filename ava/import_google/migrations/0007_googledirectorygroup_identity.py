# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0005_auto_20150715_0352'),
        ('import_google', '0006_auto_20150715_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='googledirectorygroup',
            name='identity',
            field=models.ForeignKey(default=1, to='core_identity.Identity'),
            preserve_default=False,
        ),
    ]
