from django import forms
from .models import Algorithm

class Blog_form(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Title' }))
	category = forms.CharField(widget = forms.TextInput(
		attrs = { 'class': 'algorithm-category', 'placeholder': 'Category' }))
	code = forms.CharField(widget = forms.Textarea(
		attrs = { 'class': 'code_for_algorithm', 'placeholder': 'Code', 'rows': 30, 'cols': 100 }))
	class Meta:
		model = Algorithm
		fields = ['title', 'category', 'code']