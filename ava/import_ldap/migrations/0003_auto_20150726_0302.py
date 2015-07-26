# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_ldap', '0002_remove_activedirectoryuser_logon_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activedirectoryuser',
            name='admin_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activedirectoryuser',
            name='bad_pwd_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activedirectoryuser',
            name='logon_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
