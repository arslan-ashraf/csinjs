from django import forms
from .models import Blog

class Blog_form(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Title' }))
	content = forms.CharField(widget = forms.Textarea(
		attrs = { 'class': 'code_for_blog', 'placeholder': 'Content', 'rows': 50, 'cols': 100 }))
	class Meta:
		model = Blog
		fields = ['title', 'content']