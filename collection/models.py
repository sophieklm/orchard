from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField

from geoposition.fields import GeopositionField
from django.contrib.gis.geos import Point

# Create your models here.
class Tree(models.Model):

    FRUIT = (
        ('Apple', 'Apple'),
        ('Pear', 'Pear'),
        ('Plum', 'Plum'),
    )

    TYPES = (
        ('Eater', 'Eater'),
        ('Crab', 'Crab'),
        ('Perry', 'Perry'),
        ('Cider', 'Cider'),
        ('Juicer', 'Juicer'),
        ('Cooker', 'Cooker'),
    )

    MONTHS = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )

    variety = models.CharField(max_length=255)
    fruit = models.CharField(max_length=255, choices=FRUIT)
    type = MultiSelectField(max_length=255, choices=TYPES)
    harvest = MultiSelectField(max_length=255, choices=MONTHS, blank=True)
    taste = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    position = GeopositionField(blank=True)
