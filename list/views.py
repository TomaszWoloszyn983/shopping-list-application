from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Item


# Create your views here.
def say_hello(request):
    print("Hello world")
    return render(request, "../templates/hello.html")

class ItemsList(ListView):
    model = Item
    queryset = Item.objects.order_by('-bought')
    template_name = 'base.html'

def test(request):
    print("Run testing view")
    return render(request, 'test.html')

def testwo(request):
    print("Run testing view 2")
    return render(request, 'testwo.html')