# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-24 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_mainshow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainshow',
            name='img1',
            field=models.CharField(max_length=200),
        ),
    ]
