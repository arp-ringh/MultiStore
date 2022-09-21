from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from . models import *

from apps.product.models import Product

# Create your views here.

# Create views for Front Page
# Enlist Categories
# Enlist Sub Categories
# Show Slider
# Show special offers
# Show Featured Products
# Show Recently Added Products(newest product)


class BaseView(View):
    views = {}


class frontpage(BaseView):
    def get(self, request):
        self.views['slider'] = Slider.objects.all()
        self.views['products'] = Product.objects.all()

        return render(request, 'frontpage.html',self.views)

"""
def store(request):
    views = {}
    return render(request, 'index.html', views)
"""

def contact(request):
    views = {}
    return render(request, 'contact.html', views)

def cart(request):
    views = {}
    return render(request, 'cart.html', views)

def shop(request):
    views = {}
    return render(request, 'shop.html', views)

def detail(request):
    views = {}
    return render(request, 'detail.html', views)

def checkout(request):
    views = {}
    return render(request, 'checkout.html', views)

def about(request):
    views = {}
    return render(request, 'about.html', views)

def help(request):
    views = {}
    return render(request, 'help.html', views)

def faqs(request):
    views = {}
    return render(request, 'faqs.html', views)

