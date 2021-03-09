from django.contrib import admin
from django.urls import path, include
from news.views import *

app_name = 'news'
urlpatterns = [
    path('create/', NewsCreateView.as_view(), name='create_news'),
    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('all/', NewsListView.as_view(), name='news_list'),
    path('category/all/', CategoryListView.as_view(), name='category_list'),
    path('detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('category/detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('by_category/<int:news_category_id>', NewsByCategoryView.as_view(), name='news_by_category'),
]
