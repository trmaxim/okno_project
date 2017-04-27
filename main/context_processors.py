from .models import Slider


def slider(request):
	return {'sliders':Slider.objects.all()}