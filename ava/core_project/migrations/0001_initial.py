# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core_identity', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_auth', '0001_initial'),
        ('core_group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('justification', models.TextField()),
                ('startdate', models.DateField(verbose_name='Start Date', auto_now_add=True)),
                ('enddate', models.DateField(verbose_name='End Date', null=True, blank=True)),
                ('authorisedby', models.CharField(verbose_name='Authorised By', max_length=100, blank=True, null=True)),
                ('groups', models.ManyToManyField(null=True, to='core_group.Group', blank=True)),
                ('identifiers', models.ManyToManyField(null=True, to='core_identity.Identifier', blank=True)),
                ('identities', models.ManyToManyField(null=True, to='core_identity.Identity', blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'owner'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('accesslevel', models.IntegerField(choices=[(3, 'Modify project and run tests'), (2, 'View project and run tests'), (1, 'View project')], verbose_name='Access Level', default=1)),
                ('project', models.ForeignKey(to='core_project.Project', related_name='teams')),
                ('team', models.ForeignKey(to='core_auth.Team', related_name='projects')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='projectteam',
            unique_together=set([('project', 'team')]),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name', 'owner')]),
        ),
    ]
