from django.db import models
from products.models import Product

# Order Checkout Model
class Order(models.Model):
    
    title_choices = (
        ("REVEREND", "Reverend"),
        ("SIR", "Sir"),
        ("DAME", "Dame"),
        ("MR", "Mr"),
        ("MRS", "Mrs"),
        ("MS", "Ms"),
        ("MISS", "Miss"),
    )
    title = models.CharField(max_length=50, choices=title_choices, blank=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    address_line_1 = models.CharField(max_length=40, blank=False)
    address_line_2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.country, self.first_name, self.last_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.quantity, self.product.name, self.product.price)
