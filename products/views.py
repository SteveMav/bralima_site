from django.shortcuts import render

from . models import Product 

# Create your views here.
def products_views_all(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def products_views_detail(request, id):
    products = Product.objects.all()

    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product, 'products': products})