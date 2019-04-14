# Generated by Django 2.1.3 on 2019-04-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Ширина и высота 800x400px', null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]