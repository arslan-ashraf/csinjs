from django import forms
from .models import Comment

class Comment_form(forms.ModelForm):
	content = forms.CharField(widget = forms.Textarea(
		attrs = { 'class': 'comment-form', 'placeholder': 'Type your comment here...', 'rows': 4, 'cols': 80 }))
	class Meta:
		model = Comment
		fields = ['content']