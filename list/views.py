from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.utils.text import slugify
from .models import List, Item


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
    if request.method == "POST":
        list = request.POST.get("lists_name")
        print(f'Create a new list: {list}')
        # context = {'list': list}
        # The line below is causing an error. If I replace list value 
        # with any string value new List will be added to the database.
        slugified = slugify(list)
        new_list = List(name = list, slug = slugified)
        new_list.save()
        return render(request, 'list.html')
    return render(request, 'add_list.html')

def show_lists(request):
    lists = List.objects.order_by('-create_date')
    output = ', '.join([list.name for list in lists])
    context = {'lists': lists}
    return render(request, 'list.html', context)

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