from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class List(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateField(default=timezone.now)
    date = str(timezone.now)
    name = models.CharField(blank=False, max_length=50, unique=True, default=("New List"))
    slug = models.SlugField(blank=False, max_length=50, unique=True, default=("New List"))
    # items = models.ForeignKey(Item, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ['-create_date']

    def __str__(self):
        return self.name


class Item(models.Model):
    # quantity variable type is set to char, because 
    # the quantity douesn't have to be one or two units,
    # it also can be 1 kg or 2 liters.
    id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=False, max_length=50, unique=True, default="")
    slug = models.SlugField(blank=False, max_length=50, unique=True, default="")
    quantity = models.CharField(max_length=10, default='1')
    bought = models.BooleanField(default=False)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, related_name="items")

    class Meta:
        ordering = ['-bought']

    def __str__(self):
        return self.name

