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
            name='EmailMessageType',
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
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailTest',
            fields=[
                ('test_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ava_test.Test')),
                ('fromaddr', models.EmailField(max_length=75)),
                ('subject', models.TextField(max_length=200)),
                ('body', models.TextField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
            bases=('ava_test.test',),
        ),
        migrations.CreateModel(
            name='EmailTestTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(unique=True, max_length=100)),
                ('emailtest', models.ForeignKey(to='ava_test_email.EmailTest')),
                ('target', models.ForeignKey(to='ava_core_identity.Identifier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailTestType',
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
            name='emailtesttarget',
            unique_together=set([('emailtest', 'target', 'token')]),
        ),
        migrations.AddField(
            model_name='emailtest',
            name='emailtesttype',
            field=models.ForeignKey(to='ava_test_email.EmailTestType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emailtest',
            name='messagetype',
            field=models.ForeignKey(to='ava_test_email.EmailMessageType'),
            preserve_default=True,
        ),
    ]
