import email
from pyexpat import model
from django.db import models

# Create your models here.
class users(model.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    passwordhash = models.CharField(max_length=200)
    