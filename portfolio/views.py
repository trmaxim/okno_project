from django.shortcuts import render
from django.views.generic import ListView
from .models import Images


class ListViews(ListView):
	model = Images
	paginate_by = 10
	template_name = 'portfolio/portfolio.html'


	def get_context_data(self, **kwargs):
		context = super(ListViews, self).get_context_data(**kwargs)
		return context