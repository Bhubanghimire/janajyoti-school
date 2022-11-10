# Generated by Django 4.1.3 on 2022-11-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='facebook',
            field=models.URLField(default='www.example.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='youtube',
            field=models.URLField(blank=True),
        ),
    ]
