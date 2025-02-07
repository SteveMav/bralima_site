from django.http import JsonResponse
from django.shortcuts import render, redirect
from core.models import CompanyInfo
from products.models import Product
# Create your views here.
def index(request):
    company_info = CompanyInfo.objects.all()
    return render(request, 'main/index.html', {'company_info': company_info})

def search(request):
    query = request.GET.get('q', '')
    product = Product.objects.filter(name__icontains=query) if query else []
    data = [{'id': p.id, 'name': p.name, 'image': p.image.url if p.image else ''} for p in product]
    return JsonResponse(data, safe=False)
def price_list(request):
    product_price = Product.objects.all()



    return render(request, 'main/price_list.html', {'product_price': product_price})
