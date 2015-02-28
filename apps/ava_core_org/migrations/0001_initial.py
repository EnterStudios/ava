# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_identity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupIdentifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganisationGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('grouptype', models.CharField(default=b'AD', max_length=7, verbose_name=b'Group Type', choices=[(b'AD', b'Active Directory'), (b'SO', b'Social Group'), (b'PR', b'Project'), (b'WG', b'Working Group'), (b'TE', b'Team')])),
                ('organisation', models.ForeignKey(to='ava_core_org.Organisation')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='groupidentifier',
            name='group',
            field=models.ForeignKey(to='ava_core_org.OrganisationGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupidentifier',
            name='identifier',
            field=models.ForeignKey(to='ava_core_identity.Identifier'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='groupidentifier',
            unique_together=set([('identifier', 'group')]),
        ),
    ]
