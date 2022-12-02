"""ProMed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.conf.urls import include, url

from .views import product_list, product_detail, cart, updateItem, home_page, about_page, contact_page, processOrder, service_cards_for_about, ContactView


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('models/', product_list, name='product_list'),
    path('models/<slug:slug>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('update_item/', updateItem, name='update_item'),
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('process_order/', processOrder, name='process_order'),
    path('', service_cards_for_about, name='service_cards_for_about'),
    path('contact/', ContactView.as_view(), name='contact')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)