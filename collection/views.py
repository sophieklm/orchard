from django.shortcuts import render
from collection.models import Tree

# Create your views here.
def index(request):
    trees = Tree.objects.all()
    return render(request, 'index.html', {
        'trees': trees,
})
