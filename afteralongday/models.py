import os
from django.db import models
from . import settings

# Create your models here.
class Invoice(models.Model):
    date = models.DateField(auto_now_add=True)
    contact_name = models.CharField(max_length=120)
    contact_email = models.CharField(max_length=120)
    total_price = models.IntegerField(default=0)
    orders = models.ForeignKey("Order")


class Order(models.Model):
    quantity = models.IntegerField(default=0)
    bath_bomb = models.ForeignKey('Bathbombs')

    def get_price(self):
        return self.quantity * self.bath_bomb.price

    def __str__(self):
        return "Order"

class BathBombs(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(null=True)
    image_url = models.TextField(default=settings.STATIC_URL + 'image/bathbombs/makeitmine.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bath Bomb'