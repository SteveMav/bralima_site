from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path('', views.products_views_all, name='views.products_views_all'),
    path('<int:id>/', views.products_views_detail, name='products_views_detail')
]
