# Generated by Django 4.1.3 on 2022-12-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='position',
            field=models.CharField(default='test', max_length=250),
            preserve_default=False,
        ),
    ]
