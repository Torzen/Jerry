from django.db import models

# Create your models here.
class userRegistrations(models.Model):
    username = models.CharField(max_length=100)
    email =  models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    
class users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)