from django.db import models
from accounts.models import User

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email