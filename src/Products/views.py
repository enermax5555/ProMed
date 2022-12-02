from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
# from quorum.mail import send_email
from django.views.generic import CreateView
from .models import Category, Product, Order, Customer, OrderItem, ShippingAddress, Contact
from .forms import ContactForm
from django.http import JsonResponse, HttpResponse, BadHeaderError, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import datetime
import json


# Create your views here.

def service_cards_for_about(request):
    obj = Product.objects.all()
    context = {
        'items': obj,
    }
    return render(request, 'service_cards_for_about.html', context)


def product_list(request):
    obj = Product.objects.all()
    # NEED TO BE FIXED!!! (navbar/total_cart_number)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items,
                   'order': order,
                   'object': obj}
    else:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        #     items = []
        #     order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        context = {'items': items,
                   'order': order,
                   'object': obj
                   }

    return render(request, 'models.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # NEED TO BE FIXED!!! (navbar/total_cart_number)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items,
                   'order': order,
                   'product': product}
    else:
        # items = []
        # order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        context = {'items': items,
                   'order': order,
                   'product': product}

    return render(request, 'model_details.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items,
                   'order': order}
    else:
        # items = []
        # order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items,
                   'order': order}
    return render(request, 'cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    if request.user.is_authenticated:
        customer = request.user.customer

        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
            product.stock = (product.stock - 1)
            messages.info(request, 'Item been added to cart')

        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
            product.stock = (product.stock + 1)
            messages.warning(request, 'Item been removed from cart', extra_tags='danger')
        elif action == 'remove_all':
            product.stock = (product.stock + orderItem.quantity)
            orderItem.quantity = 0
            messages.warning(request, 'All items from selected item been removed', extra_tags='danger')
        product.save()
        orderItem.save()
        if orderItem.quantity <= 0:
            orderItem.delete()
    else:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
            product.stock = (product.stock - 1)
            messages.info(request, 'Item been added to cart')

        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
            product.stock = (product.stock + 1)
            messages.warning(request, 'Item been removed from cart', extra_tags='danger')
        elif action == 'remove_all':
            product.stock = (product.stock + orderItem.quantity)
            orderItem.quantity = 0
            messages.warning(request, 'All items from selected item been removed', extra_tags='danger')
        product.save()
        orderItem.save()
        if orderItem.quantity <= 0:
            orderItem.delete()

    return JsonResponse('Item was added!', safe=False)

    # NEED FIX!!!


def home_page(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {
            'products': products,
            'items': items,
            'order': order
        }
    else:
        # items = []
        # order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items,
                   'order': order,
                   'products': products}
    return render(request, 'home.html', context)


def contact_page(request):
    # THE CODE DOWN BELLOW IS FOR THE CART NUMBER NEED TO BE REPLACED BY A FUNCTION!

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items,
                   'order': order,
                   }
    else:
        # items = []
        # order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    context = {'items': items,
               'order': order,
               }
    return render(request, 'contact.html', context)


# def contact_form(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             my_email = 'stoqn.sisimen@gmail.com'
#             body = {
#                 'name': form.cleaned_data['name'],
#                 'email': form.cleaned_data['email'],
#                 'message': form.cleaned_data['message']
#             }
#             message = "\n".join(body.values())
#
#             try:
#                 send_mail(subject, settings.EMAIL_HOST_USER, ['stoqn.sisimen@gmail.com'], fail_silently=False)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect("about.html")
#         form = ContactForm()
#         return render(request, "contact.html", {'form': form})

class ContactView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('/contact.html/')
    template_name = '/contact.html/'

    def form_invalid(self, form):
        http_header = self.request.META
        send_email(form, http_header)
        messages.error(self.request, 'Something went wrong with your submission. Please try again.')
        return HttpResponseRedirect('')

    def form_valid(self, form):
        http_header = self.request.META
        send_email(form, http_header)
        messages.success(self.request, 'Your message was submitted successfully!')
        return super().form_valid(form)


def send_email(form_data):
    # This gets the ip address of the user if u want to use it add in arguments 'http_header'!
    # (and in the print use remote_ip variable to visualization)
    # try:
    #     if http_header.get('HTTP_X_REAL_IP'):
    #         remote_ip = http_header.get('HTTP_X_REAL_IP')
    #     elif http_header.get('X-FORWARDED-FOR'):
    #         http_header.get('X-FORWARDED-FOR')
    #     else:
    #         remote_ip = 'We were not able to fetch IP Address of client'
    # except:
    #     pass

    form_message = form_data.cleaned_data['message']
    subject = form_data.cleaned_data['subject']

    try:
        email = form_data.cleaned_data['email']

    except:
        email = 'INVALID EMAIL'

        message = f'''The current message was received from {email}
    

        {form_message}
        '''

    send_mail(subject,
              message,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[settings.ADMIN_EMAIL],
              fail_silently=False)


def about_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items,
                   'order': order,
                   }
    else:
        # items = []
        # order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    context = {'items': items,
               'order': order}
    return render(request, 'about.html', context)


def processOrder(request):
    # if request.method == 'POST':
    #     print(request.POST)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    # productId = data['productId']
    # product = Product.objects.get(id=productId)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            # product.stock = product.stock - 1
            order.complete = True

        order.save()

        # if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            first_name=data['form']['First_Name'],
            last_name=data['form']['Last_Name'],
            email=data['form']['Email'],
            phone=data['form']['Phone'],
            city=data['form']['City'],
            post_code=data['form']['Zip_Code'],
            address=data['form']['Address'],
        )
    else:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            # product.stock = product.stock - 1
            order.complete = True

        order.save()

        # if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            first_name=data['form']['First_Name'],
            last_name=data['form']['Last_Name'],
            email=data['form']['Email'],
            phone=data['form']['Phone'],
            city=data['form']['City'],
            post_code=data['form']['Zip_Code'],
            address=data['form']['Address'],
        )

    return JsonResponse('Order complete!', safe=False)

# def updateItem(request):
#     if request.method == 'POST':
#         productId = request.POST['productId']
#         action = request.POST['action ']

# TESTING
# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'models.html', {'category': category,
#                                            'categories': categories,
#                                            'products': products})
#
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'model_details.html', {'product':product,
#                                                   'cart_product_form':cart_product_form})
