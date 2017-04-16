from django.shortcuts import render
from django.views.generic import ListView
from .models import Images, Jalousie, Ceiling


class ListViews(ListView):
	model = Images
	paginate_by = 10
	template_name = 'portfolio/portfolio.html'


	def get_context_data(self, **kwargs):
		context = super(ListViews, self).get_context_data(**kwargs)
		context['jalousie'] = Jalousie.objects.all()
		context['ceiling'] = Ceiling.objects.all()
		return context