from django.shortcuts import render
from collection.models import Tree

# Create your views here.
def index(request):
    trees = Tree.objects.all()

    return render(request, 'index.html', {
        'trees': trees,
})

def fruit(request):
    trees = Tree.objects.all()
    apples = Tree.objects.filter(fruit='Apple').order_by('fruit')
    pears = Tree.objects.filter(fruit='Pear').order_by('fruit')
    plums = Tree.objects.filter(fruit='Plum').order_by('fruit')
    return render(request, 'fruit.html', {
        'apples': apples,
        'pears': pears,
        'plums': plums
})

def tree_detail(request, slug):
    tree = Tree.objects.get(slug=slug)

    return render(request, 'fruit/tree_detail.html', {
        'tree': tree,
    })
