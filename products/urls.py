from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path('', views.products_views_all, name='views.products_views_all')
]
