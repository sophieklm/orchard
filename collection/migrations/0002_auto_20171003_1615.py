# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='variety',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]