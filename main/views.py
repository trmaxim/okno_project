from django.shortcuts import render
from django.views.generic.base import TemplateView
from news.models import News
from portfolio.models import Images
from django.utils import timezone



class Main(TemplateView):
	template_name = 'main/main.html'

	def get_context_data(self, **kwargs):
		context = super(Main, self).get_context_data(**kwargs)
		context['news'] = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
		context['images'] = Images.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
		return context
