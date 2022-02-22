from django.db import models

# Create your models here.
class Book(models.Model):
    BookTitle = models.CharField(max_length=1000)
    Author = models.CharField(max_length=1000)
    Publisher = models.CharField(max_length=1000)
    Genre  = models.CharField(max_length=1000)
    Year = models.CharField(max_length=1000)
    Language = models.CharField(max_length=1000)
    Description = models.TextField()
    Tags  = models.CharField(max_length=1000)
    ISBN = models.CharField(max_length=1000)