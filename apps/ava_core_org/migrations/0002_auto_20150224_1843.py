# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_org', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrganisationUnitType',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='industry',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='project',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='size',
        ),
        migrations.DeleteModel(
            name='OrganisationSize',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='user',
        ),
    ]
