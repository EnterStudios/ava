# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_twitter', '0003_auto_20150327_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twittertest',
            name='twittertesttype',
        ),
        migrations.DeleteModel(
            name='TwitterTestType',
        ),
        migrations.AlterField(
            model_name='twittertest',
            name='tweet',
            field=models.ForeignKey(verbose_name=b'Tweet', to='ava_test_twitter.TweetTemplate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twittertest',
            name='twitteraccount',
            field=models.ForeignKey(verbose_name=b'Send From Twitter Account', to='ava_test_twitter.TwitterAccount'),
            preserve_default=True,
        ),
    ]
