# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20171009_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='variety',
            field=models.CharField(max_length=255),
        ),
    ]