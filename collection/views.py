from django.shortcuts import render
thing = "Thing Name"

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'thing': thing,
})
