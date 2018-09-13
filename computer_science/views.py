from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Algorithm
from .forms import Algorithm_form

	# print("-" * 50)
	# print(form)
	# print("-" * 50)

def home(request):
	return render(request, 'home.html')

def create(request):
	if not request.user.is_superuser:
		return Http404
	form = Algorithm_form(request.POST or None)
	if form.is_valid():
		new_algorithm = form.save(commit = False)
		print(new_algorithm.cleaned_date)
		new_algorithm.save()
	items = { 'form': form }
	return render(request, 'algorithms/algorithm_form.html', items)

def categories(request):
	return

def show(request, title = None):
	algorithm = get_object_or_404(Algorithm, title = title)
	items = { 'algorithm': algorithm, }
	return 

def update(request, title = None):
	if not request.user.is_superuser:
		return Http404

def delete(request, title = None):
	if not request.user.is_superuser:
		return Http404