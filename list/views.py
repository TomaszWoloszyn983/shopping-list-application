from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

# Create your views here.
def say_hello(request):
    print("Hello world")
    return render(request, "../templates/hello.html")

class ItemsList(ListView):
    model = Item
    queryset = Item.objects.order_by('-bought')
    template_name = '../list/static/templates/base.html'