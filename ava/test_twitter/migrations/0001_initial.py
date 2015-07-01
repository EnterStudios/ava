# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0001_initial'),
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TweetTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('tweet', models.TextField(max_length=140)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('username', models.CharField(max_length=100)),
                ('password_enc', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterTest',
            fields=[
                ('test_ptr', models.OneToOneField(auto_created=True, serialize=False, to='test.Test', primary_key=True, parent_link=True)),
                ('link', models.ForeignKey(to='test_twitter.TweetLink')),
                ('tweet', models.ForeignKey(verbose_name='Tweet', to='test_twitter.TweetTemplate')),
                ('twitter_account', models.ForeignKey(verbose_name='Send From Twitter Account', to='test_twitter.TwitterAccount')),
            ],
            options={
                'abstract': False,
            },
            bases=('test.test',),
        ),
        migrations.CreateModel(
            name='TwitterTestResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ip_address', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=10)),
                ('host', models.CharField(max_length=260)),
                ('path', models.TextField(blank=True, null=True)),
                ('content_length', models.CharField(blank=True, max_length=10, null=True)),
                ('content_type', models.CharField(blank=True, max_length=100, null=True)),
                ('ua', models.TextField(blank=True, null=True)),
                ('referrer', models.TextField(blank=True, null=True)),
                ('via', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterTestTarget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('target', models.ForeignKey(to='core_identity.Identifier')),
                ('twitter_test', models.ForeignKey(to='test_twitter.TwitterTest')),
            ],
        ),
        migrations.AddField(
            model_name='twittertestresult',
            name='target',
            field=models.ForeignKey(related_name='results', to='test_twitter.TwitterTestTarget'),
        ),
        migrations.AlterUniqueTogether(
            name='twittertesttarget',
            unique_together=set([('twitter_test', 'target')]),
        ),
    ]
