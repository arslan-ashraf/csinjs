from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Algorithm
from .forms import Algorithm_form

def home(request):
	return render(request, 'home.html')

def create(request):
	if not request.user.is_superuser():
		return Http404
	form = Algorithm_form()
	return 

def categories(request):
	return

def show(request, title = None):
	algorithm = get_object_or_404(Algorithm, title = title)
	items = { 'algorithm': algorithm, }
	return 

def update(request, title = None):
	if not request.user.is_superuser():
		return Http404

def delete(request, title = None):
	if not request.user.is_superuser():
		return Http404