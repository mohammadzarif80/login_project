from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class UserModel(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    username=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=8,default=None)

class Password(models.Model):
    password=models.CharField(max_length=8)
    user=models.ForeignKey(UserModel,on_delete=CASCADE,related_name='passwords')

    
    
    
    
    