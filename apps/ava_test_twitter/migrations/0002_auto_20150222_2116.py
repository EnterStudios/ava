# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_twitter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetlink',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='tweettemplate',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='twitteraccount',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='twittertesttype',
            name='help_text',
        ),
    ]
