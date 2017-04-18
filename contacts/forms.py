from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 100)
	number = forms.CharField()
	date = forms.DateField(label = "date", widget=AdminDateWidget())
	