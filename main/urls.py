from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),
    path('prices/', views.price_list, name='price_list'),

]