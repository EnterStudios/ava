# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_core_group', '0001_initial'),
        ('ava_core_identity', '0002_auto_20150327_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifier',
            name='identity',
            field=models.ForeignKey(related_name='identifiers', to='ava_core_identity.Identity'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='identity',
            old_name='member_of',
            new_name='groups',
        ),
        migrations.AlterField(
            model_name='identity',
            name='groups',
            field=models.ManyToManyField(related_name='identities', null=True, to='ava_core_group.Group', blank=True),
            preserve_default=True,
        ),
    ]
