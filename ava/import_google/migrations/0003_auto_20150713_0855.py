# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_google', '0002_flowmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='dn',
        ),
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='emails',
        ),
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='external_ids',
        ),
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='isDelegatedAdmin',
        ),
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='org_unit_path',
        ),
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='organizations',
        ),
        migrations.RemoveField(
            model_name='googledirectoryuser',
            name='websites',
        ),
        migrations.AddField(
            model_name='googledirectoryuser',
            name='change_password_at_next_login',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='googledirectoryuser',
            name='ip_whitelisted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='googledirectoryuser',
            name='is_delegated_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='googledirectorygroup',
            name='admin_created',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='googledirectoryuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='googledirectoryuser',
            name='is_mailbox_setup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='googledirectoryuser',
            name='suspended',
            field=models.BooleanField(default=False),
        ),
    ]
