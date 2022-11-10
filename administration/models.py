from django.db import models

# Create your models here.
class About(models.Model):
    logo = models.ImageField(upload_to="logo")
    about_image = models.ImageField(upload_to="about")
    name = models.TextField(max_length=250)
    description = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    country = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    contact_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    facebook = models.URLField()
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name