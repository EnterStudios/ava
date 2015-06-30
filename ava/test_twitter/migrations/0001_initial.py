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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('description', models.TextField(verbose_name='Description', max_length=500)),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TweetTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('description', models.TextField(verbose_name='Description', max_length=500)),
                ('tweet', models.TextField(max_length=140)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('description', models.TextField(verbose_name='Description', max_length=500)),
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
                ('test_ptr', models.OneToOneField(serialize=False, to='test.Test', primary_key=True, parent_link=True, auto_created=True)),
                ('link', models.ForeignKey(to='test_twitter.TweetLink')),
                ('tweet', models.ForeignKey(verbose_name='Tweet', to='test_twitter.TweetTemplate')),
                ('twitteraccount', models.ForeignKey(verbose_name='Send From Twitter Account', to='test_twitter.TwitterAccount')),
            ],
            options={
                'abstract': False,
            },
            bases=('test.test',),
        ),
        migrations.CreateModel(
            name='TwitterTestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ipaddress', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=10)),
                ('host', models.CharField(max_length=260)),
                ('path', models.TextField(null=True, blank=True)),
                ('contentlength', models.CharField(max_length=10, blank=True, null=True)),
                ('contenttype', models.CharField(max_length=100, blank=True, null=True)),
                ('ua', models.TextField(null=True, blank=True)),
                ('referrer', models.TextField(null=True, blank=True)),
                ('via', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterTestTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('target', models.ForeignKey(to='core_identity.Identifier')),
                ('twittertest', models.ForeignKey(to='test_twitter.TwitterTest')),
            ],
        ),
        migrations.AddField(
            model_name='twittertestresult',
            name='target',
            field=models.ForeignKey(to='test_twitter.TwitterTestTarget', related_name='results'),
        ),
        migrations.AlterUniqueTogether(
            name='twittertesttarget',
            unique_together=set([('twittertest', 'target')]),
        ),
    ]
