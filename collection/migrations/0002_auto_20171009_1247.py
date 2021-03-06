# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-09 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='position',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='tree',
            name='fruit',
            field=models.CharField(choices=[('Apple', 'Apple'), ('Pear', 'Pear'), ('Plum', 'Plum')], max_length=255),
        ),
        migrations.AlterField(
            model_name='tree',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Eater', 'Eater'), ('Crab', 'Crab'), ('Perry', 'Perry'), ('Cider', 'Cider'), ('Juicer', 'Juicer'), ('Cooker', 'Cooker')], max_length=255),
        ),
    ]
