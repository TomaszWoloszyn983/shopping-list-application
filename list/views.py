from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.utils.text import slugify
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import List, Item
from .forms import ListForm, ItemForm


@login_required
def show_list_items(request, id, slug):
    '''
    The function displayes the list of items that 
    belong to the list with a slug passed as the argument.
    '''
    user = get_object_or_404(User, username=request.user)
    # lists_slug = get_object_or_404(List, slug=slug)
    list_id = get_object_or_404(List, id=id)
    if list_id.list_owner != user:
        messages.error(request, "Access denied!")
        return redirect(reverse("home"))

    items = Item.objects.filter(list_name=list_id).order_by('-id')
    bought_items = items.filter(bought=True)
    items_to_buy = items.filter(bought=False).order_by('-urgent')
    context = {
        'id': id,
        'list': list_id,
        'slug': slug,
        'items': items,
        'bought_items': bought_items,
        'items_to_buy': items_to_buy,
    }
    return render(request, 'show_list_items.html', context)


def home(request):
    '''
    Displays the Home Page
    '''
    if request.user.is_authenticated:
        lists = List.objects.filter(list_owner=request.user).order_by("-id")
        context = {
            'lists': lists,
        }
    else:
        context = {}
    return render(request, 'home.html', context)


def about(request):
    '''
    Displays the About Page
    '''
    return render(request, 'about.html')


@login_required
def add_list(request):
    '''
    Creates a new Lists and passes the list to the template
    and the database.
    '''
    list_form = ListForm(request.POST or None)
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        try:
            if list_form.is_valid():
                form = list_form.save(commit=False)
                list = request.POST.get("name")
                form.name = list
                slugified = slugify(list)
                form.slug = slugified
                form.list_owner = User.objects.get(id=request.user.id)
                form.save()
                messages.success(request, f"{list} has been created!",
                                 extra_tags='hello')
                return redirect(reverse("lists"))
        except IntegrityError as e:
            messages.error(request,
                           f"Sorry! A problem occured."
                           f"Pleasechoose another name for this list.",
                           extra_tags='invalid_name')

    lists = List.objects.order_by('-create_date')
    context = {
        'lists': lists,
        'list_form': list_form,
    }
    return render(request, 'add_list.html', context)


@login_required
def show_lists(request):
    '''
    Displays all lists created by a logged in user.
    '''
    lists = List.objects.filter(list_owner=request.user).order_by(
        '-create_date', "-id")
    context = {'lists': lists}
    return render(request, 'list.html', context)


@login_required
def edit_list(request, id, slug):
    '''
    Edit existing list by id.
    Update the lists slug.
    '''
    lists_slug = get_object_or_404(List, id=id)
    list_form = ListForm(request.POST or None, instance=lists_slug)

    if request.method == "POST":
        if list_form.is_valid():
            list = request.POST.get("name")
            list_form.instance.name = list
            slugified = slugify(list)
            list_form.instance.slug = slugified
            list_form.save()
            messages.success(request, f"List {list} has been updated!",
                             extra_tags='editlist')
            return redirect(reverse("lists"))

    context = {
        'id': id,
        'slug': slug,
        "list_form": list_form,
    }
    return render(request, 'edit_list.html', context)


@login_required
def delete_list(request, id, slug):
    '''
    Delete the list from the database.
    '''
    to_delete = get_object_or_404(List, id=id)
    to_delete.delete()
    messages.success(request, f"The list {to_delete}"
                     " has been successfully deleted!",
                     extra_tags='deletelist')
    context = {
        'id': id,
        'slug': slug
        }
    return redirect(reverse("lists"))


@login_required
def clear_list(request, id, slug):
    '''
    Delete all items from the list with given id.
    '''
    lists_slug = get_object_or_404(List, id=id)
    items = Item.objects.filter(list_name=lists_slug).order_by('bought')
    if items.delete():
        messages.success(request, "All Items have been successfully deleted"
                         " from the list", extra_tags='clearlist')
        return redirect(reverse('show_list_items',args=[
                                lists_slug.id,
                                lists_slug.slug
                                ]))

    context = {
        'id': id,
        'slug': slug,
        'items': items
    }
    return render(request, 'show_list_items.html', context)


def mark_as_bought(request, id, slug):
    """
    mark_as_bought method is nothing but items update method, where
    we only update one element of the item, which is 'bought' variable.
    """
    item = get_object_or_404(Item, id=id)
    list = get_object_or_404(List, slug=item.list_name.slug)

    if item.bought:
        item.bought = False
        item.save()
    else:
        item.bought = True
        item.save()
    return redirect(reverse('show_list_items', args=[list.id, list.slug]))


@login_required
def add_item(request, id, slug):
    '''
    Add item to the list with given id.
    '''
    list = get_object_or_404(List, id=id)
    item_form = ItemForm(request.POST or None)

    if request.method == "POST":
        try:
            if item_form.is_valid():
                name = request.POST.get("name")
                item_form.instance.slug = slugify(name)
                item_form.instance.list_name = list
                item_form.save()
                messages.success(request, f"{name} has been successfully"
                                          " added to the list!")
                return redirect(reverse("show_list_items",
                    args=[list.id, list.slug]))
        except IntegrityError as e:
            messages.error(request, f"Sorry! A problem occured. Please choose"
                           " another name for this item.", extra_tags='invalid'
                           'slug')

    context = {
        'id': id,
        "item_form": item_form,
        "slug": slug
    }
    return render(request, 'add_item.html', context)


@login_required
def delete_list_item(request, id, slug):
    '''
    Delete item from the list by requested id and from the database.
    '''
    to_delete = get_object_or_404(Item, id=id)
    if to_delete.delete():
        messages.success(request, f"Item {to_delete} has been successfully"
                         " deleted!", extra_tags='deleteitem')
        return redirect(reverse('show_list_items',
                        args=[
                            to_delete.list_name.id,
                            to_delete.list_name.slug
                        ]))
    context = {
        'id': id,
        'slug': slug
        }
    return render(request, 'delete_list_item.html', context)


@login_required
def edit_list_item(request, id, slug):
    '''
    Update items variables. Update the items slug.
    '''
    items_slug = get_object_or_404(Item, id=id)
    item_form = ItemForm(request.POST or None, instance=items_slug)

    if request.method == "POST":
        if item_form.is_valid():
            item = request.POST.get("name")
            item_form.instance.name = item
            slugified = slugify(item)
            item_form.instance.slug = slugified
            item_form.save()
            messages.success(request, f"{items_slug.name} Item has been"
                             " successfully updated!",
                             extra_tags='updateitem')
            return redirect(reverse('show_list_items',
                            args=[items_slug.list_name.id,
                            items_slug.list_name.slug]))
    context = {
        "id": id,
        'slug': slug,
        "item_form": item_form,
    }
    return render(request, 'edit_list_item.html', context)
