from django.db import models

# Create your models here.
class staffRegistration(models.Model):
    username = models.CharField( max_length=50,null=False)
    password = models.CharField( max_length = 20,null = False)
    fullname = models.CharField(max_length=100 ,null = False)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    nationality = models.CharField(max_length = 100)
    photoUrl = models.CharField(max_length = 500)
    allocateduId = models.IntegerField(null=True)
