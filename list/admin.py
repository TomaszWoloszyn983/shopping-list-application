from django.contrib import admin
from .models import List, Item
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'quantity', 'bought',
                    'favourite', 'urgent', 'price', 'description')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')


@admin.register(List)
class ListAdmin(SummernoteModelAdmin):
    list_display = ('create_date', 'name', 'slug', 'list_owner')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')
