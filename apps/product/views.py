from django.shortcuts import render, get_object_or_404, redirect

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

    return render(request, 'product/product.html', {'product':product,})
