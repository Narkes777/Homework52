from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Order, Product, Electronics, Clothing, Books

class ProductChildAdmin(PolymorphicChildModelAdmin):
    base_model = Product

@admin.register(Electronics)
class ElectronicsAdmin(ProductChildAdmin):
    base_model = Electronics

@admin.register(Clothing)
class ClothingAdmin(ProductChildAdmin):
    base_model = Clothing

@admin.register(Books)
class BooksAdmin(ProductChildAdmin):
    base_model = Books

@admin.register(Product)
class ProductParentAdmin(PolymorphicParentModelAdmin):
    base_model = Product
    child_models = (Electronics, Clothing, Books)
    list_filter = (PolymorphicChildModelFilter,)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date')
    filter_horizontal = ('products',)
