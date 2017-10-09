import csv, sys, os
from os.path import join, dirname
from django.template.defaultfilters import slugify

project_dir = join(dirname(__file__), '/fruitapp/')

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'fruitapp.settings'

import django

django.setup()

from collection.models import Tree

Tree.objects.all().delete()

data = csv.reader(open(join(dirname(__file__), 'inventory.csv')), delimiter=",")

for row in data:
    if row[0] != 'id':
        tree = Tree()
        tree.position = {'lat': float(row[2]), 'lng': float(row[1])}
        tree.field = row[3]
        tree.variety = row[4]
        tree.type = row[5].split('/')
        tree.fruit = row[6]
        tree.harvest = row[7].split('/')
        tree.taste = row[8]
        tree.slug = '-'.join((slugify(row[4]), slugify(row[6]), slugify(row[0])))
        tree.save()
