# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='dateOfSale',
            field=models.DateField(default='2017-08-12'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_models.ModelStock'),
        ),
    ]