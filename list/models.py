from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class List(models.Model):
    list_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.now)
    name = models.CharField(blank=False, max_length=30)
    slug = models.SlugField(blank=False, max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(blank=False, max_length=50)
    slug = models.SlugField(blank=False, max_length=50)
    quantity = models.CharField(max_length=7, default='1')
    bought = models.BooleanField(default=False)
    list_name = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="items")
    favourite = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True, null=True, default="")

    class Meta:
        ordering = ['-bought']

    def __str__(self):
        return self.name
