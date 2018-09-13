from django.shortcuts import render
from django.http import HttpResponse, Http404

def home(request):
	return render(request, 'home.html')

def create(request):
	if not request.user.is_superuser():
		return Http404

def categories(request):
	return

def show(request, title):
	return 

def update(request, title):
	if not request.user.is_superuser():
		return Http404

def delete(request, title):
	if not request.user.is_superuser():
		return Http404