#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=60, verbose_name="Категория")
	slug = models.SlugField(max_length=60, verbose_name='Адрес URL')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category', args=[str(self.slug)])

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural='Категории'


class News(models.Model):
	title = models.CharField(max_length=60, verbose_name = 'Заголовок')
	slug = models.SlugField(max_length=60, verbose_name = 'Адрес URL')
	body = models.TextField(max_length=500, verbose_name='Текст')
	image = models.ImageField(upload_to='media/news', verbose_name="Изображение", blank = True)
	author = models.ForeignKey(User, verbose_name="Автор")
	category = models.ForeignKey(Category, verbose_name="Категория")
	date_time = models.DateField(default=timezone.now, verbose_name="Дата создания")
	published_date = models.DateTimeField(default=timezone.now(), verbose_name="Дата публикации")


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', args=[str(self.slug)])

	class Meta:
		ordering = ['-published_date']

		verbose_name="Новость"
		verbose_name_plural = "Новости"
