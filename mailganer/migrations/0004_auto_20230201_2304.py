# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-01 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailganer', '0003_auto_20230201_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
