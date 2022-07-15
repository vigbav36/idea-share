import uuid
from django.db import models

# Create your models here.

class UserAccount(models.Model):
    Username=models.TextField()
    password=models.TextField()
    name=models.TextField()
    branch=models.TextField()
    email=models.EmailField(max_length = 254)
