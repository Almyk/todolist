from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    owner = models.CharField(max_length=200, default='stupid')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
