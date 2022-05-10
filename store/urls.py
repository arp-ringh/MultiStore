from django.urls import path
from .views import *

app_name = "store"

urlpatterns = [
    path('',store, name='store'),
    path('contact',contact, name='contact'),
    path('cart',cart, name='cart'),
    path('shop',shop, name='shop'),
    path('detail',detail, name='detail'),
    path('checkout',checkout, name='checkout'),



]

