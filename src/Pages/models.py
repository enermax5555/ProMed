from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# za julkata
# class Customer_Page(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Order_pages(models.Model):
#     customer = models.ForeignKey(Customer_Page, on_delete=models.SET_NULL, blank=True, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, blank=False, null=True)
#     transaction_id = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
#     @property
#     def get_cart_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
#
#     def get_cart_items(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.quantity for item in orderitems])
#         return total
#
