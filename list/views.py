from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.utils.text import slugify
from django.contrib import messages
from django.db import IntegrityError
from .models import List, Item, ItemExtended
from .forms import ListForm, ItemForm, ItemExForm


def showItems(request):
    items = ItemExtended.objects.order_by('-id')
    context = {'items': items}
    return render(request, 'items.html', context)

def show_list_items(request, slug):
    # Get requested elements slug
    # Get list of items filterd by mathing to the slug
    # Pass the list of items to the template
    lists_slug = get_object_or_404(List, slug=slug)
    lists = List.objects.order_by('-create_date')
    items = Item.objects.filter(list_name=lists_slug).order_by('-id')
    bought_items = items.filter(bought=True)
    items_to_buy = items.filter(bought=False)
    items_ext = ItemExtended.objects.filter(list_name=lists_slug).order_by('-id')
    bought_items_ext = items_ext.filter(bought=True)
    items_to_buy_ext = items_ext.filter(bought=False)
    context = {
        'lists': lists,
        'slug' : slug,
        'items': items,
        'bought_items': bought_items,
        'items_to_buy': items_to_buy,
        'items_ext': items_ext,
        'bought_items_ext': bought_items_ext,
        'items_to_buy_ext': items_to_buy_ext
    }
    return render(request, 'show_list_items.html', context)


# 
#   Log out users.
# 


def home(request):
    lists = List.objects.order_by("id")
    context = {
        'lists': lists
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def create_list(request):
    return render(request, 'add_list.html')


def add_list(request):
    # Validation has to be added to prevent posting elements 
    # with dublicated names.

    # Lists that contain every item with bought status should be 
    # mark with a different color than the list with not bought items.
    if request.method == "POST":
        try:
            list = request.POST.get("lists_name")
            print(f'Create a new list: {list}')
            slugified = slugify(list)
            new_list = List(name = list, slug = slugified)
            new_list.save()
            messages.success(request, f"New list {list} has been created!", extra_tags='hello')
        except IntegrityError as e:
            messages.error(request, f"List {list} already exists! Choose a different name.", extra_tags='invalid_name')

        # Redirecting to the page that displays all lists.
        lists = List.objects.order_by('-create_date')
        context = {'lists': lists}
        return render(request, 'list.html', context)
    return render(request, 'add_list.html')

def show_lists(request):
    lists = List.objects.order_by('-create_date', "-id")
    # Output isn't propably used.
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
            list_form.name = list
            slugified = slugify(list)
            print(f'Slugified: {slugified}')
            list_form.slug = slugified
            list_form.save()
            messages.success(request, f"List {list} has been updated!", extra_tags='editlist')
            return redirect(reverse("lists"))

    context = {
        'slug': slug,
        "list_form": list_form,
    }
    return render(request, 'edit_list.html', context)

def delete_list(request, slug):
    to_delete = get_object_or_404(List, slug=slug)
    print(f'Deleteing {to_delete} list')
    to_delete.delete()
    messages.success(request, f"The list {to_delete} has been successfully deleted!", extra_tags='deletelist')
    context = {'slug': slug}
    return render(request, 'delete_list.html', context)

def clear_list(request, slug):
    lists_slug = get_object_or_404(List, slug=slug)
    items = Item.objects.filter(list_name=lists_slug).order_by('bought')
    if items.delete():
        messages.success(request, "All Items have been successfully deleted from the List", extra_tags='clearlist')
        return redirect(reverse('show_list_items', args=[lists_slug.slug]))

    context = {
        'slug' : slug,
        'items': items
    }
    return render(request, 'show_list_items.html', context)

# The name should be changed to add_item and create_item tempalate deleted
def create_item(request, slug):
    list = get_object_or_404(List, slug=slug)
    item_form = ItemForm(request.POST or None)

    if request.method == "POST":
        if item_form.is_valid():
            item_form.instance.slug = slugify(request.POST.get("name"))
            item_form.instance.list_name = list
            item_form.save()
            return redirect(reverse("show_list_items", args=[list.slug]))

    context = {
        "item_form": item_form,
        "slug": slug
    }
    return render(request, 'add_item.html', context)

def delete_item(request, slug):
    to_delete = get_object_or_404(Item, slug=slug)
    print(f'Deleteing {to_delete} item')
    if to_delete.delete():
        messages.success(request, f"Item {to_delete} has been successfully deleted!", extra_tags='deleteitem')
        return redirect(reverse('show_list_items', args=[to_delete.list_name.slug]))
    
    context = {'slug': slug}
    return render(request, 'delete_item.html', context)

def edit_item(request, slug):
    items_slug = get_object_or_404(Item, slug=slug)
    print(f'Editing {items_slug} element')
    item_form = ItemForm(request.POST or None, instance=items_slug)

    if request.method == "POST":
        if item_form.is_valid():
            item_form.save()
            messages.success(request, f"Item has been successfully updated!", extra_tags='updateitem')
            return redirect(reverse('show_list_items', args=[items_slug.list_name.slug]))

    context = {
        'slug': slug,
        "item_form": item_form,
    }
    return render(request, 'edit_item.html', context)

def mark_as_bought(request, slug):
# mark_as_bought method is nothing but items update method, where
# we only update one element of the item, which is 'bought' variable.
# The problem may be to call the mark_as_bought method.
    item = get_object_or_404(Item, slug=slug)
    list = get_object_or_404(List, slug=item.list_name.slug)
    print(f'\n\nMarking {item} as bought/notbought')

    if item.bought:
        item.bought = False
        print(f'Update {item} to False')
        item.save()
    else:
        item.bought = True
        print(f'Update {item} to True')
        item.save()
    return redirect(reverse('show_list_items', args=[list.slug]))

# 
#   Log in users section
# 

def showItems(request):
    items = ItemExtended.objects.order_by('-id')
    context = {'itemsextended': items}
    return render(request, 'items.html', context)

# 
# I need to extract items list and to get that lists slug
def create_extended_item(request):
    # list = get_object_or_404(List)
    lists = List.objects.order_by("-id")
    items = ItemExtended.objects.order_by('-id')
    item_form = ItemExForm(request.POST or None)

    if request.method == "POST":
        if item_form.is_valid():
            item_form.instance.slug = slugify(request.POST.get("name"))
            # item_form.instance.list_name = list
            item_form.save()
            # context = {'itemsextended': items}
            # return render(request, 'items.html', context)
            return redirect(reverse('items'))

    context = {
        "item_form": item_form,
    }
    return render(request, 'create_extended_item.html', context)

def add_ext_item(request, slug):
    list = get_object_or_404(List, slug=slug)
    item_ex_form = ItemExForm(request.POST or None)

    if request.method == "POST":
        if item_ex_form.is_valid():
            item_ex_form.instance.slug = slugify(request.POST.get("name"))
            item_ex_form.instance.list_name = list
            item_ex_form.save()
            return redirect(reverse("show_list_items", args=[list.slug]))

    context = {
        "item_ex_form": item_ex_form,
        "slug": slug
    }
    return render(request, 'add_ext_item.html', context)
    

def delete_ext_item(request, slug):
    to_delete = get_object_or_404(ItemExtended, slug=slug)
    items = ItemExtended.objects.order_by('bought')
    print(f'Deleteing {to_delete} item')
    if to_delete.delete():
        messages.success(request, f"The item {to_delete} has been successfully deleted!", extra_tags='deletelist')
        return redirect(reverse("items"))
    context = {'slug': slug}
    return render(request, 'delete_list.html', context)
    

def edit_ext_item(request, slug):
    items_slug = get_object_or_404(ItemExtended, slug=slug)
    items = ItemExtended.objects.order_by('bought')
    print(f'Editing {items_slug} element')
    item_form = ItemExForm(request.POST or None, instance=items_slug)

    if request.method == "POST":
        if item_form.is_valid():
            item_form.save()
            messages.success(request, f"Item has been successfully updated!", extra_tags='updateitem')
            context = {'itemsextended': items}
            return redirect(reverse("items"))

    context = {
        'slug': slug,
        "item_form": item_form,
    }
    return render(request, 'edit_ext_item.html', context)


def clear_list(request, slug):
    lists_slug = get_object_or_404(List, slug=slug)
    items = ItemExtended.objects.filter(list_name=lists_slug).order_by('bought')
    if items.delete():
        messages.success(request, "All Items have been successfully deleted from the List", extra_tags='clearlist')
        return redirect(reverse('show_list_items', args=[lists_slug.slug]))

    context = {
        'slug' : slug,
        'items': items
    }
    return render(request, 'show_list_items.html', context)


def mark_as_bought_ext(request, slug):
# mark_as_bought method is nothing but items update method, where
# we only update one element of the item, which is 'bought' variable.
# The problem may be to call the mark_as_bought method.
    item = get_object_or_404(ItemExtended, slug=slug)
    list = get_object_or_404(List, slug=item.list_name.slug)
    print(f'\n\nMarking {item} as bought/notbought')

    if item.bought:
        item.bought = False
        print(f'Update {item} to False')
        item.save()
    else:
        item.bought = True
        print(f'Update {item} to True')
        item.save()
    return redirect(reverse('show_list_items', args=[list.slug]))

# Clear extended list function has to be created
# Add extended item for show_ext_list_item function has to be created.
# 
# 