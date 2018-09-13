from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Algorithm
from .forms import Algorithm_form
from django.db.models import Count

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
		return redirect('computer_science:title',
						friendly_title = new_algorithm.friendly_title, 
						permanent = True)
	items = { 'form': form, 'title': 'Create New Algorithm' }
	return render(request, 'algorithms/algorithm_form.html', items)

def update(request, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
	form = Algorithm_form(request.POST or None, instance = algorithm)
	if form.is_valid():
		updated_algorithm = form.save(commit = False)
		updated_algorithm.save()
		return redirect('computer_science:title', 
						friendly_title = updated_algorithm.friendly_title, 
						permanent = True)
	items = { 'form': form, 'title': 'Update Algorithm' }
	return render(request, 'algorithms/algorithm_form.html', items)	

def categories(request):
	algorithms = Algorithm.objects.all()
	hashmap = {}
	for algorithm in algorithms:
		hashmap[algorithm.category] = 1 
	items = { 'all_categories': list(hashmap) }
	print("-" * 50)
	print(list(hashmap))
	print("-" * 50)
	return render(request, 'algorithms/categories.html', items)

def show(request, friendly_title = None):
	algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
	items = { 'algorithm': algorithm, }
	return 

def delete(request, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
	algorithm.delete()
	return redirect("computer_science:base", permanent = True)

def search(request):
	return 