from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Idea(models.Model):
    title = models.TextField(max_length=255)
    short_description = models.TextField(null=True)
    long_description = models.TextField(null=True)
    created_by = models.ForeignKey(User,related_name='ideas',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def job_id(self):
        return self.id

class Idea_applicants(models.Model):
    user = models.ForeignKey(User,related_name='ideas_user',on_delete=models.CASCADE)
    job_id = models.ForeignKey(Idea,related_name='ideas_id',on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    skills = models.TextField(blank=False)