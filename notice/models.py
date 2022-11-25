from django.db import models


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    publish_date = models.DateField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
