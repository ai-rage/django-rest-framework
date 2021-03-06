from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Restaurant(models.Model):
    title 	  = models.CharField(max_length=100, blank=True, default='Название')
    longitude = models.FloatField(max_length=100)
    latitude  = models.FloatField(max_length=100)
    image	 = models.ImageField(
			null=True, blank=True,
			upload_to='images/',
			verbose_name='Изображение'
			)

class Product(models.Model):
	name	 = models.CharField(max_length=100, blank=True, default='Название')
	price	 = models.IntegerField()
	category = models.IntegerField()
	image	 = models.ImageField(
			null=True, blank=True,
			upload_to='images/',
			verbose_name='Изображение'
			)
