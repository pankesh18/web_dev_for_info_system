from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)


    objects = models.Manager()


    