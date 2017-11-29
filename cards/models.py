from __future__ import unicode_literals
from django.db import models
from categories.models import Category

class Card(models.Model):
    name = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, null=False, blank=False, related_name="cards")
    
    def __str__(self):
        return self.name