# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import oauth2client.django_orm


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('import_google', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowModel',
            fields=[
                ('id', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('flow', oauth2client.django_orm.FlowField(null=True)),
            ],
        ),
    ]
