# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-09 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20171009_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='field',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tree',
            name='harvest',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=255),
        ),
    ]
