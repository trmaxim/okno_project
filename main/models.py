#-*- coding: utf-8 -*-

from django.db import models

class Slider(models.Model):
	title = models.CharField(max_length=30, verbose_name="Заголовок")
	body = models.TextField(max_length=300, verbose_name = "Текст")
	image = models.ImageField(upload_to='media/slider', verbose_name="Изображение")
	url = models.CharField(max_length=50, verbose_name="Ссылка")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural='Слайдер'