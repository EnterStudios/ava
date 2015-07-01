# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('test_type', models.CharField(max_length=7, choices=[('EMAIL', 'Email'), ('TWITTER', 'Twitter')], verbose_name='Test Type', default='EMAIL')),
                ('test_status', models.CharField(max_length=10, choices=[('NEW', 'New'), ('COMPLETE', 'Complete'), ('ERROR', 'An error occurred'), ('SCHEDULED', 'Scheduled'), ('RUNNING', 'In progress')], verbose_name='Test Status', default='NEW')),
                ('redirect_url', models.CharField(blank=True, max_length=2000, null=True)),
                ('page_template', models.CharField(blank=True, max_length=100, null=True)),
                ('project', models.ForeignKey(null=True, to='core_project.Project', related_name='tests')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
