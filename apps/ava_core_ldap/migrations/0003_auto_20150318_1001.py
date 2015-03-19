# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_ldap', '0002_auto_20150316_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activedirectoryuser',
            name='groups',
            field=models.ManyToManyField(related_name='users', to='ava_core_ldap.ActiveDirectoryGroup'),
            preserve_default=True,
        ),
    ]
