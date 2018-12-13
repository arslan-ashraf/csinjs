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
		print(new_algorithm)
		new_algorithm.save()
		return redirect(new_algorithm,
						new_algorithm.get_absolute_url,
						permanent = True)
	items = { 'form': form, 'title': 'Create New Algorithm', 'value': 'Create' }
	return render(request, 'algorithms/algorithm_form.html', items)

def update(request, friendly_category = None, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
	form = Algorithm_form(request.POST or None, instance = algorithm)
	if form.is_valid():
		updated_algorithm = form.save(commit = False)
		updated_algorithm.save()
		return redirect(updated_algorithm,
						# friendly_category = updated_algorithm.friendly_category,
						# friendly_title = updated_algorithm.friendly_title,
						updated_algorithm.get_absolute_url,
						permanent = True)
	items = { 'form': form, 'title': 'Update Algorithm', 'value': 'Update' }
	return render(request, 'algorithms/algorithm_form.html', items)

def categories(request):
	algorithms = Algorithm.objects.all()
	# print('%' * 50)
	# print(algorithms.count())
	# print('%' * 50)
	hashmap = {}
	for algorithm in algorithms:
		hashmap[algorithm.category] = algorithm.friendly_category
	items = { 'all_categories': hashmap, 'title': 'Categories of Algorithms' }
	return render(request, 'algorithms/categories.html', items)

def index(request, friendly_category = None):
	type_of_algorithms = Algorithm.objects.filter(friendly_category = friendly_category)
	items = { 'algorithms': type_of_algorithms, 'title': type_of_algorithms[0].category }
	return render(request, 'algorithms/index.html', items)

def show(request, friendly_category = None, friendly_title = None):
	algorithm = Algorithm.objects.filter(friendly_title = friendly_title)
	if not algorithm:
		return Http404
	# print('#' * 50)
	# print(algorithm[0].comment_set.all()[0].content)
	# print('#' * 50)
	items = { 'algorithm': algorithm[0], 
			  'title': algorithm[0].title, 
			  'comments': algorithm[0].comment_set.all() }
	return render(request, 'algorithms/show.html', items)

def delete(request, friendly_category = None, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	algorithm = Algorithm.objects.filter(friendly_title = friendly_title)
	if not algorithm:
		return Http404
	algorithm.delete()
	return redirect("computer_science:home", permanent = True)

def search(request):
	searched_text = request.POST['searched_text']
	if len(searched_text) == 0:
		return render(request, 'algorithms/search_results.html', { 'results': []})
	algorithms = Algorithm.objects.filter(title__icontains = searched_text)[:5]

	items = { 'results': algorithms }
	return render(request, 'algorithms/search_results.html', items)