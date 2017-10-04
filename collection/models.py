from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Tree(models.Model):

    FRUIT = (
        ('Apple', 'Apple'),
        ('Pear', 'Pear'),
        ('Gage', 'Gage'),
    )

    TYPES = (
        ('Eater', 'Eater'),
        ('Crab', 'Crab'),
        ('Perry', 'Perry'),
        ('Cider', 'Cider'),
        ('Juicer', 'Juicer'),
        ('Cooker', 'Cooker'),
    )

    variety = models.CharField(max_length=255, unique=True)
    fruit = models.CharField(max_length=255, choices=FRUIT)
    type = MultiSelectField(max_length=255, choices=TYPES)
    harvest = models.CharField(max_length=255, blank=True)
    taste = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

