from django.contrib import admin
from administration.models import ContactUs, About, Staff, Testimonials


# Register your models here.
@admin.register(ContactUs)
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ["id"]