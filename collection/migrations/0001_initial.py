# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('fruit', models.CharField(max_length=255)),
                ('harvest', models.CharField(max_length=255)),
                ('taste', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
