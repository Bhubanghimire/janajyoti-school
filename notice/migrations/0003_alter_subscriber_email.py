# Generated by Django 4.1.3 on 2022-11-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
