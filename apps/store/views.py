from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View

from django.contrib.auth import login, logout
from django.contrib import messages, auth


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
        self.views['offer_first'] = Offer.objects.all()[0:2]
        self.views['offer_second'] = Offer.objects.all()[2:4]


        # self.views['featured_products'] = Product.objects.filter(labels= 'featured')
        # self.views['recent_products'] = Product.objects.filter(labels= '')[0:8]

        featured_products = Product.objects.filter(labels= 'featured')[0:8]
        # self.views['featured_products'] = get_object_or_404(featured_products)
        if featured_products.exists():
            self.views['featured_products'] = get_list_or_404(featured_products)

        recent_products = Product.objects.filter(labels= '')[0:8]
        if recent_products.exists():
            self.views['recent_products'] = get_list_or_404(recent_products)

        return render(request, 'store/frontpage.html',self.views)

"""
def store(request):
    views = {}
    return render(request, 'index.html', views)
"""

def contact(request):
    views = {}
    return render(request, 'store/contact.html', views)

def cart(request):
    views = {}
    return render(request, 'store/cart.html', views)

def shop(request):
    views = {}
    return render(request, 'store/shop.html', views)

def detail(request):
    views = {}
    return render(request, 'store/detail.html', views)

def checkout(request):
    views = {}
    return render(request, 'store/checkout.html', views)

def about(request):
    views = {}
    return render(request, 'store/about.html', views)

def help(request):
    views = {}
    return render(request, 'store/help.html', views)

def faqs(request):
    views = {}
    return render(request, 'store/faqs.html', views)



def logout(request):
    auth.logout(request)
    return redirect('/')
