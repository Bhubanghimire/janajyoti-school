from django.contrib import admin
from notice.models import Notice, Subscriber

# Register your models here.
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_by", "created_at"]

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "created_at"]


