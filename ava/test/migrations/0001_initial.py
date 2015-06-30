# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core_project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('description', models.TextField(verbose_name='Description', max_length=500)),
                ('testtype', models.CharField(choices=[('EMAIL', 'Email'), ('TWITTER', 'Twitter')], max_length=7, default='EMAIL', verbose_name='Test Type')),
                ('teststatus', models.CharField(choices=[('NEW', 'New'), ('COMPLETE', 'Complete'), ('ERROR', 'An error occurred'), ('SCHEDULED', 'Scheduled'), ('RUNNING', 'In progress')], max_length=10, default='NEW', verbose_name='Test Status')),
                ('redirect_url', models.CharField(max_length=2000, blank=True, null=True)),
                ('page_template', models.CharField(max_length=100, blank=True, null=True)),
                ('project', models.ForeignKey(null=True, to='core_project.Project', related_name='tests')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
