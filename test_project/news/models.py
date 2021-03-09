from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Категория', db_index=True, unique=True, max_length=100)
    COLORS = (
        (1, "red"),
        (2, "green"),
        (3, "blue"),
        (4, "yellow"),
        )
    color = models.IntegerField(verbose_name='Цвет', choices=COLORS)

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(verbose_name='Название', db_index=True, unique=True, max_length=255)
    short_description = models.CharField(verbose_name='Краткое описание', max_length=500)
    full_description = models.CharField(verbose_name='Полное описание', max_length=3000)
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
