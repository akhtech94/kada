from shops.models import Shop
from django.db import models

class Product(models.Model):
    name            = models.CharField(max_length=25, blank=False, null=False)
    available       = models.IntegerField(blank=False, null=False)
    rate            = models.IntegerField(blank=False, null=False)
    quality         = models.IntegerField(blank=True, null=True)
    colour          = models.CharField(max_length=25, blank=True, null=True)
    specification   = models.CharField(max_length=25, blank=True, null=True)
    shop            = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
