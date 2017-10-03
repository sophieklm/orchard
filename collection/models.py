from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fruit(models.Model):
    variety = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    fruit = models.CharField(max_length=255)
    harvest = models.CharField(max_length=255)
    taste = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
