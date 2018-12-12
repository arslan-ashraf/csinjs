from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from .forms import Login_form, Registration_form, Edit_profile_form, Change_password_form
from ajax.models import Notification

def user_login(request):
	form = Login_form(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username = username, password = password)
		if user:
			login(request, user)
			return redirect("user:profile", permanent = True)
	items = { 'form': form, 'title': 'Login', 'value': 'Login', 'info': 'Sign In' }
	return render(request, 'users/user_form.html', items)

def create(request):
	# print('()' * 50)
	# print('create')
	# print('()' * 50)
	form = Registration_form(request.POST or None)
	if form.is_valid():
		new_user = form.save()
	# 	print(new_user)
		if new_user:
			login(request, new_user)
		return redirect('user:profile', permanent = True)
	items = { 'form': form, 'title': 'Register', 'value': 'Sign Up', 'info': 'Register' }
	return render(request, 'users/user_form.html', items)

@login_required
def update(request, friendly_title = None):
	# print('|' * 50)
	# print(request)
	# print('|' * 50)
	form = Edit_profile_form(request.POST or None, instance = user)
	if form.is_valid():
		form.save()
		return redirect('users:profile', permanent = True)
	# 	# print('x' * 50)
	# 	# print(x)
	# 	# print('x' * 50)
	items = { 'form': form, 'title': 'Edit Profile', 'value': 'Save Changes', 'info': 'Edit Profile' }
	return render(request, 'users/user_form.html', items)

@login_required
def profile(request):
	items = { 'user': request.user, 'title': 'Profile', 'comments': 'n/a' } #request.user.comments_set.all() }
	return render(request, 'users/user_profile.html', items)

def change_password(request):
	form = Change_password_form(data = request.POST or None, user = request.user)
	if form.is_valid():
		form.save()
		update_session_auth_hash(request, form.user)
		return redirect('users:profile', permanent = True)
	items = { 'user': request.user, 'title': 'Change Password', 'value': 'Save Password', 'info': 'Change Password' }
	return render(request, 'users/user_form.html', items)

@login_required
def delete(request, friendly_title = None):
	logout(request)
	return redirect('computer_science:home', permanent = True)