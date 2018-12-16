from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from .forms import Login_form, Registration_form, Edit_profile_form, Change_password_form
from comments.models import Comment, Notification

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

@login_required
def user_logout(request):
	print('x' * 50)
	print(request.user)
	print('x' * 50)
	logout(request)
	return redirect('computer_science:home', permanent = True)

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
	# print('update profile')
	# print(request)
	# print('|' * 50)
	form = Edit_profile_form(request.POST or None, instance = request.user)
	if form.is_valid():
		form.save()
		return redirect('user:profile', permanent = True)
	items = { 'form': form, 'title': 'Edit Profile', 'value': 'Save Changes', 'info': 'Edit Profile' }
	return render(request, 'users/user_form.html', items)

@login_required
def profile(request):
	items = { 'user': request.user, 'title': 'Profile', 'comments': request.user.comment_set.all() }
	return render(request, 'users/user_profile.html', items)

@login_required
def change_password(request):
	form = Change_password_form(data = request.POST or None, user = request.user)
	if form.is_valid():
		form.save()
		update_session_auth_hash(request, form.user)
		return redirect('users:profile', permanent = True)
	items = { 'form': form, 'user': request.user, 'title': 'Change Password', 'value': 'Save Password', 'info': 'Change Password' }
	return render(request, 'users/user_form.html', items)

@login_required
def	delete(request):
	user = request.user
	user.delete()
	return redirect('computer_science:home', permanent = True)

def user_notifications(request):
    if not request.user.is_authenticated:
        return JsonResponse([], safe = False)
    all_notifications_of_this_user = Notification.objects.filter(receiver = request.user)
    data_arr = []
    for i in range(0, len(all_notifications_of_this_user)):
        data = {}
        data['sender'] = all_notifications_of_this_user.sender
        data['action'] = all_notifications_of_this_user.action
        data['body'] = all_notifications_of_this_user.body
        data['url'] = all_notifications_of_this_user.url
        data_arr.append(data)
    return JsonResponse(data_arr, safe = False)