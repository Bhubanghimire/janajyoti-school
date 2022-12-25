# Generated by Django 4.1.3 on 2022-12-25 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'CONFIG CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='ConfigChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='category')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.configcategory', verbose_name='choice')),
            ],
            options={
                'verbose_name_plural': 'CONFIG CHOICE',
            },
        ),
    ]
