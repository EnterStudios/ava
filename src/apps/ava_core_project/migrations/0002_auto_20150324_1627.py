# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_auth', '__first__'),
        ('ava_core_identity', '0001_initial'),
        ('ava_core_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('accesslevel', models.IntegerField(default=1, verbose_name=b'Access Level', choices=[(3, b'Modify project and run tests'), (2, b'View project and run tests'), (1, b'View project')])),
                ('project', models.ForeignKey(related_name='teams', to='ava_core_project.Project')),
                ('team', models.ForeignKey(related_name='projects', to='ava_core_auth.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='projectteam',
            unique_together=set([('project', 'team')]),
        ),
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='group',
            new_name='groups',
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name', 'owner')]),
        ),
        migrations.AddField(
            model_name='project',
            name='identifiers',
            field=models.ManyToManyField(to='ava_core_identity.Identifier', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='identities',
            field=models.ManyToManyField(to='ava_core_identity.Identity', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='authorisedby',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Authorised By', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='enddate',
            field=models.DateField(default=timezone.now(), verbose_name=b'End Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='justification',
            field=models.TextField(default='Sample justification'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='startdate',
            field=models.DateField(default=timezone.now(), auto_now_add=True, verbose_name=b'Start Date'),
            preserve_default=False,
        ),
    ]
