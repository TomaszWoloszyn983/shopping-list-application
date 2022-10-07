from django.contrib import admin
from .models import Item

# @admin.site.register(Item)
# class ItemAdmin(Item):
#     prepopulated_fields = {'slug': ('name',)}