# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_group', '0001_initial'),
        ('import_google', '0007_googledirectorygroup_identity'),
    ]

    operations = [
        migrations.AddField(
            model_name='googledirectorygroup',
            name='group',
            field=models.ForeignKey(to='core_group.Group', blank=True, null=True),
        ),
    ]
