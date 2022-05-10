from django.shortcuts import render

# Create your views here.
def store(request):
    views = {}
    return render(request, 'index.html', views)

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

