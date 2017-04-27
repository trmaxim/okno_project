#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone



class Images(models.Model):
	name = models.CharField(max_length=30, verbose_name="Название")
	description = models.TextField(max_length=200, verbose_name="Описание")
	image = models.ImageField(upload_to='media/portfolio', verbose_name="Изображение", blank=True)
	pub_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.name


	class Meta:
		ordering = ['pub_date']
		verbose_name="Портфолио"
		verbose_name_plural = "Портфолио"