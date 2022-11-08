from django.contrib import admin
from system.models import ConfigCategory, ConfigChoice
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(ConfigCategory)
class ConfigCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]

@admin.register(ConfigChoice)
class ConfigChoiceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category"]


admin.site.unregister(Group)
