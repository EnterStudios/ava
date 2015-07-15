# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0004_auto_20150715_0116'),
        ('import_google', '0004_googledirectorygroup_direct_members_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credentialsmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='flowmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='googledirectoryuser',
            name='identity',
            field=models.ManyToManyField(to='core_identity.Identity'),
        ),
        migrations.DeleteModel(
            name='CredentialsModel',
        ),
        migrations.DeleteModel(
            name='FlowModel',
        ),
    ]
