# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0008_identity_groups'),
        ('import_google', '0010_remove_googledirectoryuser_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='googledirectoryuser',
            name='identity',
            field=models.ForeignKey(to='core_identity.Identity', default=1),
            preserve_default=False,
        ),
    ]
