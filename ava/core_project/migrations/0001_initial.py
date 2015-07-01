# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core_auth', '0001_initial'),
        ('core_identity', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('justification', models.TextField()),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Start Date')),
                ('enddate', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('authorised_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Authorised By')),
                ('groups', models.ManyToManyField(blank=True, null=True, to='core_group.Group')),
                ('identifiers', models.ManyToManyField(blank=True, null=True, to='core_identity.Identifier')),
                ('identities', models.ManyToManyField(blank=True, null=True, to='core_identity.Identity')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'owner'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('access_level', models.IntegerField(choices=[(3, 'Modify project and run tests'), (2, 'View project and run tests'), (1, 'View project')], verbose_name='Access Level', default=1)),
                ('project', models.ForeignKey(related_name='teams', to='core_project.Project')),
                ('team', models.ForeignKey(related_name='projects', to='core_auth.Team')),
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
