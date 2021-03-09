from django.shortcuts import render
from rest_framework import generics
from news.serializers import *
from news.models import News

# Create your views here.
class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsDetailSerializer

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer

class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()

class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()

class NewsByCategoryView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()

    def get(self, request, news_category_id):
        self.queryset = News.objects.filter(news_category=news_category_id)
        return super().get(request, news_category_id)
