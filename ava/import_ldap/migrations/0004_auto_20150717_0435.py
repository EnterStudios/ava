# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_ldap', '0003_auto_20150713_2333'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ldapconfiguration',
            unique_together=set([('server', 'dump_dn')]),
        ),
    ]
