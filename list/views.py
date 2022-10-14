from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import Item
from .models import List


# Create your views here.
class ItemsList(ListView):
    model = Item
    itemslist = Item.objects.order_by('-bought')
    template_name = 'items.html'

def showItems(request):
    items = Item.objects.order_by('bought')
    output = ', '.join([item.name for item in items])
    context = {'items': items}
    return render(request, 'items.html', context)

def home(request):
    return render(request, 'home.html')

def lists(request):
    return render(request, 'list.html')

def create_list(request):
    return render(request, 'add_list.html')

def add_list(request):
    print('Creating new list')
    if request.method == "POST":
        print('The Method is POST')
        # username = request.GET.get('username','')
        # list = List(lists_name=request.form.get("lists_name"))
        list = request.GET.get("lists_name")
        print(f'New lists name is {list}')
        return render(request, 'add_list.html', list)
    return render(request, 'add_list.html')

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