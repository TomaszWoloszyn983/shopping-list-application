from django.contrib import admin
from .models import Item
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Item)
class ItemAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'quantity', 'bought')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')