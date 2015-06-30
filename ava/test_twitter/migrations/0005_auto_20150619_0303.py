# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_twitter', '0004_auto_20150617_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetlink',
            name='description',
            field=models.TextField(max_length=500, verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweetlink',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweettemplate',
            name='description',
            field=models.TextField(max_length=500, verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweettemplate',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='description',
            field=models.TextField(max_length=500, verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Name'),
            preserve_default=True,
        ),
    ]
