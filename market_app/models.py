from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=225)
    description = models.TextField()
    net_worth = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    markets = models.ManyToManyField(Market, related_name='sellers')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    market = models.ManyToManyField(Market, related_name='products')
    seller = models.ManyToManyField(Seller, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.price})"