import os
from django.db import models
from django.conf import settings

# Create your models here.
class Invoice(models.Model):
    date = models.DateField(auto_now_add=True)
    contact_name = models.CharField(max_length=120)
    contact_email = models.CharField(max_length=120)
    total_price = models.IntegerField(default=0)
    bath_bombs = models.ForeignKey('BathBombs', on_delete=models.CASCADE, null=True)

    def add_bath_bomb(self, bath_bomb):
        self.total_price += bath_bomb.price

class BathBombs(models.Model):
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=120, default=0)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=os.path.join(settings.STATICFILES_DIRS[0], 'img', 'bathbombs'), null=True)

    # Return the image filename if set otherwise return placeholder
    def filename(self):
        if self.image is not None:
            return os.path.basename(self.image.name)
        return 'bathbomb_placeholder.jpg'

    def get_price(self):
        if "$" not in self.price:
            return "%s %s" % ("$", self.price)
        return self.price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bath Bomb'