from django import template
from main.models import Slider

register = template.Library()


@register.inclusion_tag('slider/slider.html')
def show_slider():
	slider = Slider.objects.all()
	return {'slider':slider}