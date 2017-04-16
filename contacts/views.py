from django.shortcuts import render
from .forms import ContactForm
from django.utils import timezone

def contact(request):
	form = ContactForm(request.POST)
	if form.is_valid():
		model_instanse = form.save(commit=False)
		model_instanse.date_time = timezone.now()
		model_instanse.save()

	else:
		form = ContactForm()

	return render(request,'contacts/contact.html', {'form':form})
