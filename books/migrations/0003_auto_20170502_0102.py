# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170502_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]