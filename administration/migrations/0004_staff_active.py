# Generated by Django 4.1.3 on 2022-12-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_staff_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
