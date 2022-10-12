from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Item


# Create your views here.
class ItemsList(ListView):
    model = Item
    queryset = Item.objects.order_by('-bought')
    template_name = 'items.html'

def home(request):
    return render(request, 'home.html')

def items(request):
    return render(request, 'items.html')

def addItem(request):
    print("Add items method")
    return render(request, 'add_item.html')

def say_hello(request):
    print("Hello world")
    return render(request, "../templates/hello.html")

def test(request):
    print("Run testing view")
    return render(request, 'test.html')

def testwo(request):
    print("Run testing view 2")
    return render(request, 'testwo.html')