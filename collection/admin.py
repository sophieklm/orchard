from django.contrib import admin

# Register your models here.
from collection.models import Fruit

class FruitAdmin(admin.ModelAdmin):
    model = Fruit
    list_display = ('variety', 'fruit', 'type', 'harvest', 'taste', 'description',)
    prepopulated_fields = { 'slug': ('variety',)}

admin.site.register(Fruit, FruitAdmin)
