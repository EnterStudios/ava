# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ava_test_email', '0002_emailtestresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtest',
            name='html_body',
        ),
        migrations.AddField(
            model_name='emailtest',
            name='is_html',
            field=models.BooleanField(default=False, verbose_name=b'Send as HTML Email?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtest',
            name='body',
            field=models.TextField(verbose_name=b'Message Body'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtest',
            name='fromaddr',
            field=models.EmailField(max_length=75, verbose_name=b'Send From Email Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailtest',
            name='subject',
            field=models.CharField(max_length=200, verbose_name=b'Subject'),
            preserve_default=True,
        ),
    ]
