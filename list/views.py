from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.utils.text import slugify
from .models import List, Item
from .forms import ListForm


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
    # Validation has to be added to prevent posting elements 
    # with dublicated names.

    # Lists that contain every item with bought status should be 
    # mark with a different color than the list with not bought items.
    if request.method == "POST":
        list = request.POST.get("lists_name")
        print(f'Create a new list: {list}')
        slugified = slugify(list)
        new_list = List(name = list, slug = slugified)
        new_list.save()

        # Redirecting to the page that displays all lists.
        lists = List.objects.order_by('-create_date')
        output = ', '.join([list.name for list in lists])
        context = {'lists': lists}
        return render(request, 'list.html', context)
    return render(request, 'add_list.html')

def show_lists(request):
    lists = List.objects.order_by('-create_date')
    output = ', '.join([list.name for list in lists])
    context = {'lists': lists}
    return render(request, 'list.html', context)

def edit_list(request, slug):
    lists_slug = get_object_or_404(List, slug=slug)
    print(f'Editing {lists_slug} element')
    list_form = ListForm(request.POST or None, instance=lists_slug)

    if request.method == "POST":
        if list_form.is_valid():
            list = request.POST.get("name")
            print(f'Received from POST: {list}')
            slugified = slugify(list)
            list_form.name = list
            list_form.slug = slugified
            list_form.save()
            return redirect(reverse("lists"))

    context = {
        'slug': slug,
        "list_form": list_form,
    }
    return render(request, 'edit_list.html', context)

def delete_list(request, slug):
    to_delete = get_object_or_404(List, slug=slug)
    print(f'Deleteing {to_delete} element')
    to_delete.delete()
    context = {'slug': slug}
    return render(request, 'delete_list.html', context)


def items(request):
    return render(request, 'items.html')

def addItem(request):
    print("Add items method")
    return render(request, 'add_item.html')

def say_hello(request):
    print("Hello world")
    return render(request, "../templates/hello.html")

def testwo(request):
    print("Run testing view 2")
    return render(request, 'testwo.html')