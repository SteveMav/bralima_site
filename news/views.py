from django.shortcuts import render, redirect
from . models import News


def news_views_all(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})


# Create your views here.
