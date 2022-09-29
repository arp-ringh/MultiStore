from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
import random

from .models import Category, Subcategory, Product
# Create your views here.


def category(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category':category, })


def subcategory(request, category_slug, subcategory_slug):
    subcategory = get_object_or_404(Subcategory, category__slug=category_slug, slug=subcategory_slug)

    return render(request, 'product/subcategory.html', {'subcategory':subcategory, })


def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    # Similar Products Section
    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >=4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product/product.html', {'product':product, 'similar_products':similar_products, })

def search(request):
    query = request.GET.get('query', '')
    search_name=query
    products = Product.objects.filter(Q(name__icontains=query))

    return render(request, 'product/search.html', {'products':products, 'query':query, 'search_name':search_name,})
