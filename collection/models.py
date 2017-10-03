from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=255)
    fruit = models.CharField(max_length=255)

    def __unicode__(self):
        return u'{0}'.format(self.type)

class Fruit(models.Model):
    variety = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255)
    fruit = models.CharField(max_length=255)
    harvest = models.CharField(max_length=255, blank=True)
    taste = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

