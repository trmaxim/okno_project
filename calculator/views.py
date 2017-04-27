from django.shortcuts import render
from .forms import CalculatorForm
res = {}
def add(request):
	if request.method == 'POST':
		form = CalculatorForm(request.POST)
		
		if form.is_valid():
			w = form.cleaned_data['w']
			h = form.cleaned_data['h']
			b = form.cleaned_data['b']
			
		r = w * 20 + h * 50 + b *2
		res['value'] = r
	else:
		#Заполняем форму
		form = CalculatorForm()
	#Отправляем форму на страницу
	return render(request, 'calc/c.html', {'form': form, 'res':res})
