import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    Username=models.TextField(primary_key=True)
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.TextField()
    name=models.TextField()
    branch=models.TextField()
    email=models.EmailField(max_length = 254)
    
