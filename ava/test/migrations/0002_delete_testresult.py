# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestResult',
        ),
    ]
