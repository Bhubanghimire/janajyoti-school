from django.contrib import admin
from administration.models import ContactUs, About


# Register your models here.
@admin.register(ContactUs)
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]