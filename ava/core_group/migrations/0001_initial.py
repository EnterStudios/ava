# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('group_type', models.CharField(default=b'GENERIC', max_length=20, verbose_name=b'Group Type', choices=[(b'ACTIVE DIRECTORY', b'Active Directory'), (b'SOCIAL GROUP', b'Social Group'), (b'PROJECT', b'Project'), (b'WORKING GROUP', b'Working Group'), (b'TEAM', b'Team'), (b'GENERIC', b'Generic Group'), (b'ORGANISATION', b'Organisation'), (b'DISTRIBUTION LIST', b'Distribution List')])),
                ('parent', models.ForeignKey(blank=True, to='ava_core_group.Group', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together=set([('name', 'group_type')]),
        ),
    ]
