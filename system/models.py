from django.db import models

class ConfigCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "CONFIG CATEGORY"


    def __str__(self):
        return self.name


class ConfigChoice(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="category", null=True, blank=True)
    category = models.ForeignKey(ConfigCategory, on_delete=models.CASCADE, verbose_name="choice")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural = "CONFIG CHOICE"
