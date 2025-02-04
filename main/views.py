from django.shortcuts import render, redirect
from core.models import CompanyInfo
# Create your views here.
def index(request):
    Company_info = CompanyInfo.objects.all()
    return render(request, 'main/index.html', {'Company_info': Company_info})
