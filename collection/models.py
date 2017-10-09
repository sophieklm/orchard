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
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )

    variety = models.CharField(max_length=255)
    field = models.CharField(max_length=255, blank=True)
    fruit = models.CharField(max_length=255, choices=FRUIT)
    type = MultiSelectField(max_length=255, choices=TYPES)
    harvest = MultiSelectField(max_length=255, choices=MONTHS, blank=True)
    taste = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    position = GeopositionField(blank=True)
