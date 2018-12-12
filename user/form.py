from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class Login_form(forms.Form):
	username = forms.CharField(widget = forms.TextInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Username'}))
	password = forms.CharField(widget = forms.PasswordInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Password'}))

	class Meta:
		model = user 
		fields = ['username', 'password']

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		user = authenticate(username = username, password = password)
		if not user:
			raise forms.ValidationError('Incorrect username and/or password')



class Registration_form(UserCreationForm):
	username = forms.CharField(widget = forms.TextInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Username'}))
	email = forms.EmailField(required = False, widget = forms.EmailInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Email'}))
	password1 = forms.CharField(widget = forms.PasswordInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Password'}))
	password2 = forms.CharField(widget = forms.PasswordInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Confirm password'}))

	class Meta:
		model = user 
		fields = ['username', 'email', 'password1', 'password2']



class Edit_profile_form(UserChangeForm):
	username = forms.CharField(widget = forms.TextInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Username'}))
	email = forms.EmailField(required = False, widget = forms.EmailInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Email'}))
	password = forms.CharField(widget = forms.PasswordInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Password'}))

	class Meta:
		model = user 
		fields = ['username', 'email', 'password']

	def clean_password(self):
		entered_password = self.cleaned_data['password']
		user = authenticate(username = self.instance.username, password = entered_password)
		if not user:
			raise forms.ValidationError('Please enter the correct password')
		return self.initial['password']


class Change_password_form(PasswordChangeForm):
	old_password = forms.CharField(widget = forms.PasswordInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Current Password'}))
	new_password1 = forms.CharField(widget = forms.PasswordInput(
		attrs = { 'class': 'input-text', 'placeholder': 'New password'}))
	new_password2 = forms.CharField(widget = forms.PasswordInput(
		attrs = { 'class': 'input-text', 'placeholder': 'Confirm new password'}))

	class Meta:
		model = user 
		fields = ['old_password', 'new_password1', 'new_password2']

	def clean_old_password(self):
		entered_old_password = self.cleaned_data['old_password']
		if not self.user.check_password(entered_old_password):
			raise forms.ValidationError('Please enter the correct password')
		return entered_old_password