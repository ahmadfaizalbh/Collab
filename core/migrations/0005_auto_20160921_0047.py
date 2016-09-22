# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160921_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
