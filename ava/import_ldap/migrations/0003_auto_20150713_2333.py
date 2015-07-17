# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_ldap', '0002_auto_20150710_0019'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ldapconfiguration',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='ldapconfiguration',
            name='user_dn',
        ),
        migrations.RemoveField(
            model_name='ldapconfiguration',
            name='user_pw',
        ),
    ]
