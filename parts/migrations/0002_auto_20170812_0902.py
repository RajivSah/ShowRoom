# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part_processing',
            name='out_date',
            field=models.DateField(default='2017-08-12'),
        ),
        migrations.AlterField(
            model_name='part_stock',
            name='entry_date',
            field=models.DateField(default='2017-08-12'),
        ),
    ]