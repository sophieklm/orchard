from django.contrib import admin
from django import forms

# Register your models here.
from collection.models import Type, Fruit

class FruitForm(forms.ModelForm):
    FRUITS=Type.objects.values('fruit').distinct()
    TYPES=Type.objects.values('type').distinct()
    fruit = forms.ModelChoiceField(queryset=FRUITS, to_field_name="fruit")
    type = forms.ModelChoiceField(queryset=TYPES, to_field_name="type")
    def __init__(self, *args, **kwargs):
        fruitid = kwargs.pop('fruit', None)
        super(FruitForm, self).__init__(*args, **kwargs)

        if fruitid:
            self.fields['type'].queryset = Type.objects.filter(fruit=fruitid)
    class Meta:
        model = Fruit
        fields = ['variety', 'fruit', 'type', 'harvest', 'taste', 'description', 'slug']
        widgets = {
            'variety': forms.TextInput(attrs={'placeholder': 'Barland'}),
            'harvest': forms.TextInput(attrs={'placeholder': 'September-October'}),
            'taste': forms.TextInput(attrs={'placeholder': 'Sweet'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description here'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Autopopulated URL'}),
        }

class FruitAdmin(admin.ModelAdmin):
    model = Fruit
    list_display = ('variety', 'fruit', 'type', 'harvest', 'taste', 'description',)
    prepopulated_fields = { 'slug': ('variety',)}
    form = FruitForm

class TypeAdmin(admin.ModelAdmin):
    model = Type
    list_display = ('fruit', 'type')

admin.site.register(Type, TypeAdmin)
admin.site.register(Fruit, FruitAdmin)
