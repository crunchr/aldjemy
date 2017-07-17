# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 09:51
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20170705_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='tictactoeboard',
            name='array_of_decimals',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=1, max_digits=3), default=None, size=9, null=True, blank=True),
            preserve_default=False,
        ),
    ]
