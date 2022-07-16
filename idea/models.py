from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Idea(models.Model):
    title = models.TextField(max_length=255)
    short_descirption = models.TextField()
    long_description = models.TextField()
    created_by = models.ForeignKey(User,related_name='ideas',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
