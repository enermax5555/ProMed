from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Products:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 default='Basic Category', db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, default='no_image_available2.png')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    stock = models.PositiveIntegerField(default=1)
    short_desc = models.TextField(default='paste desc', null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Products:product_detail', args=[self.id, self.slug])

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Testing_index(models.Model):
    test = models.TextField()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.available == False:
                shipping == True
            return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def fresh_stock(self):
        Product.stock = (Product.stock - self.quantity)
        self.save()
        return self.product.stock


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    phone = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    city = models.CharField(max_length=20, null=True)
    post_code = models.DecimalField(max_digits=6, decimal_places=0, null=True)
    address = models.CharField(max_length=30, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.address


class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    massage = models.TextField(max_length=2000, null=True, blank=True)
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
    # Delete Test
    # def delete(self, *args, **kwargs):
    #     self.clear_nullable_related()
    #     super(Product, self).delete(*args, **kwargs)
    #
    # def clear_nullable_related(self):
    #     for related in self._meta.get_all_related_objects():
    #         accessor = related.get_accessor_name()
    #         related_set = getattr(self, accessor)
    #
    #         if related.field.null:
    #             related_set.clear()
    #         else:
    #             for related_object in related_set.all():
    #                 related_object.clear_nullable_related()