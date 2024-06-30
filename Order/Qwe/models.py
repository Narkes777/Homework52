from django.db import models
from polymorphic.models import PolymorphicModel

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=255)
    products = models.ManyToManyField('Product', related_name='orders')

class Product(PolymorphicModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Electronics(Product):
    warranty_period = models.CharField(max_length=50)

class Clothing(Product):
    size = models.CharField(max_length=10)
    material = models.CharField(max_length=100)

class Books(Product):
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
