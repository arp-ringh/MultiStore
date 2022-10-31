from django.urls import path
#from .views import *
from . import views

app_name = "cart"

urlpatterns = [
    path('cart/', views.cart_detail, name='cart'),
    path('success/', views.success, name='success'),
    ]
