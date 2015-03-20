# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0001_initial'),
        ('ava_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TweetTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('tweet', models.TextField(max_length=140)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('password_enc', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterTest',
            fields=[
                ('test_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ava_test.Test')),
                ('link', models.ForeignKey(to='ava_test_twitter.TweetLink')),
                ('tweet', models.ForeignKey(to='ava_test_twitter.TweetTemplate')),
                ('twitteraccount', models.ForeignKey(to='ava_test_twitter.TwitterAccount')),
            ],
            options={
                'abstract': False,
            },
            bases=('ava_test.test',),
        ),
        migrations.CreateModel(
            name='TwitterTestTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('target', models.ForeignKey(to='ava_core_identity.Identifier')),
                ('twittertest', models.ForeignKey(to='ava_test_twitter.TwitterTest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterTestType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='twittertesttarget',
            unique_together=set([('twittertest', 'target')]),
        ),
        migrations.AddField(
            model_name='twittertest',
            name='twittertesttype',
            field=models.ForeignKey(to='ava_test_twitter.TwitterTestType'),
            preserve_default=True,
        ),
    ]
