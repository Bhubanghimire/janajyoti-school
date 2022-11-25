from django.contrib import admin
from notice.models import Subscriber


# Register your models here.
@admin.register(Subscriber)
class Subscriber(admin.ModelAdmin):
    list_display = ["id", "email", "created_at"]
