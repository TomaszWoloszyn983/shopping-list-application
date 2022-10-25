from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.utils.text import slugify
from .models import List, Item
from .forms import ListForm, ItemForm


def showItems(request):
    items = Item.objects.order_by('bought')
    # output = ', '.join([item.name for item in items])
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
            list_form.name = list
            slugified = slugify(list)
            print(f'Slugified: {slugified}')
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


def show_list_items(request, slug):
    # Get requested elements slug
    # Get list of items filterd by mathing to the slug
    # Pass the list of items to the template
    lists_slug = get_object_or_404(List, slug=slug)
    items = Item.objects.filter(list_name=lists_slug).order_by('bought')
    context = {
        'slug' : slug,
        'items': items
    }
    return render(request, 'show_list_items.html', context)

def add_item(request):
    lists = List.objects.order_by('-create_date')
    # I'm not sure about the code below. It's suppose to initailize the item form
    # item_slug = get_object_or_404(Item)
    item_form = ItemForm(request.POST or None)
    # if item_form.is_valid():
    if request.method == "POST":
        name = request.POST.get("items_name")
        quantity = request.POST.get("quantity")
        slugified = slugify(name)
        list_name = List(request.POST.get("list_name")).id
        list_id = 0
        for list in lists:
            if(list.name==list_name):
                print(f'\n\nCondition met for: {list.name}. Compare to {list_name}')
                list_id = list.id

        print(f'Try to dispaly {list_name} id: {list_id}')
        print(f'Creating a new item: {name}, quantity: {quantity}')
        new_item = Item(
                name = name, 
                slug = slugified, 
                quantity = quantity,
                list_name = List(request.POST.get('list_id'))
        )
        new_item.save()
        # item_form.name = item
        # item_form.slug = slugified
        # item_form.quantity = quantity
        # item_list = list that we add this item to.
        # item_form.save()
        return redirect(reverse("lists"))
    return render(request, 'add_item.html', {'lists': lists})

def create_item(request):
    item_form = ItemForm(request.POST or None)

    if request.method == "POST":
        if item_form.is_valid():
            item = request.POST.get("name")
            quantity = request.POST.get("quantity")
            print(f'Received from POST: {item}')
            slugified = slugify(item)
            # item_form.name = item
            # item_form.slug = slugified

            print(f'Create_item: {item} slug {slugified}')

            new_item = Item(
                name = item, 
                slug = slugified, 
                quantity = quantity,
                list_name = List(request.POST.get('list_id'))
            )
            print(f'\nPrinting the new item: {new_item}')
            # item_form.save()
            new_item.save()
            return redirect(reverse("items"))

    context = {
        "item_form": item_form,
    }
    return render(request, 'create_item.html', context)

def delete_item(request, slug):
    to_delete = get_object_or_404(Item, slug=slug)
    print(f'Deleteing {to_delete} element')
    to_delete.delete()
    context = {'slug': slug}
    return render(request, 'delete_item.html', context)

def edit_item(request, slug):
    items_slug = get_object_or_404(Item, slug=slug)
    print(f'Editing {items_slug} element')
    item_form = ItemForm(request.POST or None, instance=items_slug)

    if request.method == "POST":
        if item_form.is_valid():
            item = request.POST.get("name")
            print(f'Received from POST: {item}')
            slugified = slugify(list)
            item_form.name = item
            item_form.slug = slugified
            item_form.save()
            return redirect(reverse("items"))

    context = {
        'slug': slug,
        "item_form": item_form,
    }
    return render(request, 'edit_item.html', context)

def mark_as_bought(request, slug):
# mark_as_bought method is nothing but items update method, where
# we only update one element of the item, which is 'bought' variable.
# The only problem may be to call the mark_as_bought method.
    items_slug = get_object_or_404(Item, slug=slug)
    # lists_slug = get_object_or_404(List, slug=slug)
    # items = Item.objects.filter(list_name=lists_slug).order_by('bought')
    print(f'\n\nMarking {items_slug} as bought/notbought')

    if request.method == "POST":
        print(f'Method POST is working')
        if item_slug.bought == False:
            item_slug.bought = True
            print(f'Update {item_slug} to True')
        else:
            item_slug.bought = False
            print(f'Update {item_slug} to False')

    # context = {
    #     'slug': slug,
    #     'items': items
    # }
    return HttpResponseRedirect(reverse('show_list_items', args=[items_slug]))