from django.utils import timezone

from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    city_publish = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year_published = models.DateField(default=timezone.now())
    page_count = models.IntegerField()
    sell_count = models.IntegerField()
