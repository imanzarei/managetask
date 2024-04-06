from django.contrib.auth.models import User
from django.db import models
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('TO DO', 'To Do'),
        ('IN PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO DO')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
