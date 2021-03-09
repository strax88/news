from rest_framework import serializers
from news.models import News, Category


class NewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'