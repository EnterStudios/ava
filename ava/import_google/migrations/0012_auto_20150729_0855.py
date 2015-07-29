# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_google', '0011_googledirectoryuser_identity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='googledirectoryuser',
            options={'ordering': ['first_name', 'surname', 'google_id']},
        ),
        migrations.AlterField(
            model_name='googledirectorygroup',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterUniqueTogether(
            name='googledirectorygroup',
            unique_together=set([('google_id', 'google_configuration')]),
        ),
        migrations.AlterUniqueTogether(
            name='googledirectoryuser',
            unique_together=set([('google_id', 'google_configuration')]),
        ),
    ]
