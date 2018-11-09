# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-21 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
        migrations.DeleteModel(
            name='img',
        ),
    ]
