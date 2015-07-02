# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='groups',
            field=models.ManyToManyField(blank=True, to='core_group.Group'),
        ),
        migrations.AlterField(
            model_name='project',
            name='identifiers',
            field=models.ManyToManyField(blank=True, to='core_identity.Identifier'),
        ),
        migrations.AlterField(
            model_name='project',
            name='identities',
            field=models.ManyToManyField(blank=True, to='core_identity.Identity'),
        ),
    ]
