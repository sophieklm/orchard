from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tree(models.Model):

    FRUIT = (
        ('apple', 'Apple'),
        ('pear', 'Pear'),
        ('gage', 'Gage'),
    )

    TYPES = (
        ('eater', 'Eater'),
        ('crab', 'Crab'),
        ('perry', 'Perry'),
        ('cider', 'Cider'),
        ('juicer', 'Juicer'),
        ('cooker', 'Cooker'),
    )


    variety = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255, choices=TYPES)
    fruit = models.CharField(max_length=255, choices=FRUIT)
    harvest = models.CharField(max_length=255, blank=True)
    taste = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

