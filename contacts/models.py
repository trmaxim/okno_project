#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Contacts(models.Model):
	first_name = models.CharField(max_length=30, verbose_name="Имя")
	last_name = models.CharField(max_length=30, verbose_name="Фамилия")
	number = models.CharField(max_length=12, verbose_name="Номер для связи")
	message = models.TextField(max_length=300, verbose_name="Текст письма")
	date_time = models.DateTimeField(default=timezone.now())


	def __str__(self):
		return self.first_name


	class Meta:
		verbose_name_plural = 'Письма'
