from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import DateInput


class ContactForm(forms.Form):
	name = forms.CharField(max_length = 100)
	number = forms.CharField()
	date = forms.DateField(widget=DateInput)


	class Media:
		css = {'all': ('pretty.css',)}
		js = ('animations.js', 'actions.js')