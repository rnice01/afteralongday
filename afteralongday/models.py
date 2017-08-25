import os
from django.db import models
from django.conf import settings

# Create your models here.
class Invoice(models.Model):
    date = models.DateField(auto_now_add=True)
    contact_name = models.CharField(max_length=120)
    contact_email = models.CharField(max_length=120)
    total_price = models.IntegerField(default=0)


class Order(models.Model):
    bath_bomb = models.OneToOneField('BathBombs', null=True)
    quantity = models.IntegerField(default=0)

    def get_price(self):
        return self.bath_bomb.price * self.quantity

class BathBombs(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='image/bathbombs', null=True)

    # Return the image filename if set otherwise return placeholder
    def filename(self):
        if self.image is not None:
            return os.path.basename(self.image.name)
        return 'bathbomb_placeholder.jpg'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bath Bomb'