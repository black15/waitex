from django.contrib import admin
from .models import Category, Customer, Product, Order, OrderItem, ShippingAddress

admin.site.register(Category)
admin.site.register(Customer)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = ({'slug': ('name',)})

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)