# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('import_ldap', '0003_auto_20150726_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='activedirectoryuser',
            name='lockoutTime',
            field=models.CharField(default=datetime.datetime(2015, 7, 26, 3, 25, 50, 976289, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
