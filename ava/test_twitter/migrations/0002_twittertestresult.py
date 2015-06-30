# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterTestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ipaddress', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=10)),
                ('host', models.CharField(max_length=260)),
                ('path', models.TextField(null=True, blank=True)),
                ('contentlength', models.CharField(max_length=10, null=True, blank=True)),
                ('contenttype', models.CharField(max_length=100, null=True, blank=True)),
                ('ua', models.TextField(null=True, blank=True)),
                ('referrer', models.TextField(null=True, blank=True)),
                ('via', models.TextField(null=True, blank=True)),
                ('target', models.ForeignKey(related_name='results', to='ava_test_twitter.TwitterTestTarget')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
