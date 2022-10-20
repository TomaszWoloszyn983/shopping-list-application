from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class List(models.Model):
    create_date = models.DateField(default=timezone.now)
    name = models.CharField(blank=False, max_length=50, unique=True, default=("New List"))
    slug = models.SlugField(blank=False, max_length=50, unique=True, default=("new_list"))

    # class Meta:
    #     ordering = ['-create_date']

    def __str__(self):
        return self.name


class Item(models.Model):
    # quantity variable type is set to char, because 
    # the quantity douesn't have to be one or two units,
    name = models.CharField(blank=False, max_length=50, unique=True, default="")
    slug = models.SlugField(blank=False, max_length=50, unique=True, default="")
    quantity = models.CharField(max_length=5, default='1')
    bought = models.BooleanField(default=False)
    list_name = models.ForeignKey(List, on_delete=models.CASCADE, related_name="items", default="None")

    class Meta:
        ordering = ['-bought']

    def __str__(self):
        return self.name

