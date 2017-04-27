from django import forms



class ContactForm(forms.Form):
	name = forms.CharField(max_length = 100)
	number = forms.CharField(max_length=12)
	message = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'}))
