from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='products', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    item_number = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.name, self.item_number)
