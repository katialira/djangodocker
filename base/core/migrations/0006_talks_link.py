# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-10 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_human_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='talks',
            name='link',
            field=models.URLField(default='http://google.com'),
            preserve_default=False,
        ),
    ]
