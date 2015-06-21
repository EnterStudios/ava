# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_import_ldap', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activedirectorygroup',
            options={'ordering': ['cn', 'distinguishedName']},
        ),
        migrations.AlterModelOptions(
            name='activedirectoryuser',
            options={'ordering': ['cn', 'distinguishedName']},
        ),
    ]
