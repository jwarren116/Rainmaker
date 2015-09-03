from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='products')
    price = models.DecimalField(decimal_places=2)
    item_number = models.IntegerField()
