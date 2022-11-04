from django import forms
from .models import List, Item, ItemExtended


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ("name",)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "slug", "quantity", "list_name")

class ItemExForm(forms.ModelForm):
    class Meta:
        model = ItemExtended
        fields = ("name", "slug", "quantity", "list_name",
                  "favourite", "urgent", 'price', 'description')
