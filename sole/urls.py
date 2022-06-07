"""sole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from core.views import frontpage, contact, about
from coupon.api import api_can_use
from store.views import product_detail, category_detail
from cart.views import cart_detail, success
from cart.webhook import webhook
from store.api import api_add_to_cart, api_remove_from_cart, api_checkout, create_checkout_session

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('cart/', cart_detail, name='cart_detail'),
    path('hooks/', webhook, name='webhook'),
    path('cart/success/', success, name='success'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),

    # api
    path('can_use/', api_can_use, name='api_can_use'),
    path('create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    path('api_add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api_remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    path('checkout/', api_checkout, name='api_checkout'),
    
    # store

    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
