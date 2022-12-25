from django.db import models
from system.models import ConfigChoice


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

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "staff")
    position = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE, null=True)
    facebook = models.URLField()
    contact = models.CharField(max_length=10)
    instagram = models.CharField(max_length=30, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class Testimonials(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=250)
    image = models.ImageField(upload_to="staff")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
