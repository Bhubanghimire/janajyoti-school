# Generated by Django 4.1.3 on 2022-11-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo')),
                ('about_image', models.ImageField(upload_to='about')),
                ('name', models.TextField(max_length=250)),
                ('description', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('contact_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
