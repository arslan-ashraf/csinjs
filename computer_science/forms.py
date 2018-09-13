from django import forms
from .models import Algorithm

class Algorithm_form(forms.Form):
	class Meta:
		model = Algorithm
		fields = ['title', 'category', 'code']