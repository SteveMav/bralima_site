from django.shortcuts import render, redirect
from . models import Product 

# Create your views here.
def products_views_all(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})
