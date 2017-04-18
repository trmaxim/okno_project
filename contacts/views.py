from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
	
		if form.is_valid():
			name = form.cleaned_data['name']
			number = form.cleaned_data['number']
			date = form.cleaned_data['date']
			
			try:
				you_admin_email = ['int_var@mail.ru']
				send_mail(name, number, date, you_admin_email)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'contacts/thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'contacts/contact.html', {'form': form})