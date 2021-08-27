from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=150, default='NA')
    password = models.CharField(max_length=10, default='NA')
