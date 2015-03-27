# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_twitter', '0002_twittertestresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetlink',
            name='description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweettemplate',
            name='description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twittertesttype',
            name='description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
    ]
