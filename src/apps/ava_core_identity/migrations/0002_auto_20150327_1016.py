# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='identifier',
            options={'ordering': ['identifiertype', 'identifier']},
        ),
        migrations.AlterModelOptions(
            name='identity',
            options={'ordering': ['name'], 'verbose_name': 'identity', 'verbose_name_plural': 'identities'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['surname', 'firstname'], 'verbose_name': 'person', 'verbose_name_plural': 'people'},
        ),
        migrations.AlterField(
            model_name='identity',
            name='description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
    ]
