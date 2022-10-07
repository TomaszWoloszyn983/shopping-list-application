from django.db import models

class Item(models.Model):
    # quantity variable type is set to char, because 
    # the quantity douesn't have to be one or two units,
    # it also can be 1 kg or 2 liters.
    name = models.CharField(blank=False, max_length=50, unique=True, default="")
    slug = models.SlugField(blank=False, max_length=50, unique=True, default="")
    quantity = models.CharField(max_length=10, default='1')
    bought = models.BooleanField(default=False)

    class Meta:
        # Items displaying order. Its going to have to be modified.
        ordering = ['-bought']

    def __str__(self):
        return self.name