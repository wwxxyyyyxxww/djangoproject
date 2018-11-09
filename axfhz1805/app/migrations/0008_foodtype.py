# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-24 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180924_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=50)),
                ('typename', models.CharField(max_length=50)),
                ('childtypenames', models.CharField(max_length=100)),
                ('typesort', models.IntegerField(max_length=50)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
