from django import forms



class CalculatorForm(forms.Form):
	w = forms.IntegerField()
	h = forms.IntegerField()
	b = forms.IntegerField()

