from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
from django.utils import timezone

class ListNews(ListView):
	model = News
	template_name = 'news/list.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(ListNews, self).get_context_data(**kwargs)
		context['news'] = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:4]
		return context



class DetailNews(DetailView):
	model = News
	template_name = 'news/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailNews, self).get_context_data(**kwargs)
		context['new'] = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:4]
		return context