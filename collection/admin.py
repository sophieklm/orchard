from django.contrib import admin
from django import forms

# Register your models here.
from collection.models import Tree

class TreeAdmin(admin.ModelAdmin):
    model = Tree
    list_display = ('variety', 'fruit', 'type', 'harvest', 'taste', 'description',)
    prepopulated_fields = { 'slug': ('variety',)}

admin.site.register(Tree, TreeAdmin)
