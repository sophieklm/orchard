from django.shortcuts import render
from collection.models import Tree
import operator
from django.db.models import Q

# Create your views here.
def index(request):
    trees = Tree.objects.all()
    varieties = Tree.objects.values('variety').distinct()
    months = Tree.objects.values('harvest').distinct()
    eater = reduce(operator.and_, (Q(type__contains=item) for item in [u'Eater']))
    eaters = Tree.objects.filter(eater)
    juicer = reduce(operator.and_, (Q(type__contains=item) for item in [u'Juicer']))
    juicers = Tree.objects.filter(juicer)
    brewer = reduce(operator.and_, (Q(type__contains=item) for item in [[u'Perry'], [u'Cider']]))
    brewers = Tree.objects.filter(brewer)
    cooker = reduce(operator.and_, (Q(type__contains=item) for item in [u'Cooker']))
    cookers = Tree.objects.filter(cooker)

    return render(request, 'index.html', {
        'trees': trees,
        'varieties': varieties,
        'months': months,
        'eaters': eaters,
        'juicers': juicers,
        'brewers': brewers,
        'cookers': cookers,
})

def fruit(request):
    trees = Tree.objects.all()
    apples = Tree.objects.filter(fruit='Apple').order_by('variety')
    pears = Tree.objects.filter(fruit='Pear').order_by('variety')
    plums = Tree.objects.filter(fruit='Plum').order_by('variety')
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
