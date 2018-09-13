from django.shortcuts import render, get_object_or_404, redirect
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
		return redirect(new_algorithm, permanent = True)
	items = { 'form': form }
	return render(request, 'algorithms/algorithm_form.html', items)

def update(request, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
	form = Algorithm_form(request.POST or None, instance = algorithm)
	if form.is_valid():
		updated_algorithm = form.save(commit = False)
		updated_algorithm.save()
		return redirect(updated_algorithm, permanent = True)
	items = { 'form': form }
	return render(request, 'algorithms/algorithm_form.html', items)	

def categories(request):
	all_categories = Algorithm.objects.all()
	return

def show(request, friendly_title = None):
	algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
	items = { 'algorithm': algorithm, }
	return 

def update(request, friendly_title = None):
	if not request.user.is_superuser:
		return Http404

def delete(request, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
	algorithm.delete()
	return redirect("computer_science:base", permanent = True)