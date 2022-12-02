from django.contrib import admin

# Register your models here.
from .models import Product, Category, Testing_index, Order, OrderItem, Customer, ShippingAddress, Contact


admin.site.site_header = 'ProMed'

admin.site.register(Testing_index)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created', 'updated', 'available']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'image',
                    'description', 'price', 'stock', 'created',
                    'updated', 'available']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']


admin.site.register(Category)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem, OrderItemAdmin)


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'phone', 'city', 'post_code', 'address',
                    'date_added']


admin.site.register(ShippingAddress, ShippingAdmin)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']


admin.site.register(Contact, ContactFormAdmin)