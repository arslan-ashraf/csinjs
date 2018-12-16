from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Algorithm
from .forms import Algorithm_form
from django.db.models import Count
from comments.models import Comment
from comments.forms import Comment_form

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
	if (request.method == 'POST'):
	    new_comment = Comment.objects.create(user = request.user,
	                                         algorithm = algorithm,
	                                         content = request.POST['typed_comment'],
	                                        )
	    for each_user in algorithm.users.all():
	        if each_user == request.user:
	            continue
	        Notification.objects.create(sender = request.user.username,
                                        receiver = each_user.username,
                                        action = 'posted a',
                                        body = 'comment',
                                        url = algorithm.get_absolute_url()
                                        )
        algorithm.users.add(request.user)
        return render(request, 'comments/new_comment.html', { 'comment': new_comment })
	# print('#' * 50)
	# print(algorithm[0].comment_set.all()[0].content)
	# print('#' * 50)
	form = Comment_form(request.POST or None)
	current_user_likes = False
    like_or_unlike = 'Like'
    if request.user.is_authenticated:
        if request.user in algorithm.likes.all():
            current_user_likes = True
        if current_user_likes:
            like_or_unlike = 'Unlike'
	items = { 'algorithm': algorithm[0],
			  'title': algorithm[0].title,
			  'comments': algorithm[0].comment_set.all(),
			  'form': form,
			  'value': 'Submit Comment',
			  'like_or_unlike': like_or_unlike, }
	return render(request, 'algorithms/show.html', items)

@login_required
def algorithm_like(request, friendly_category = None, friendly_title = None):
    algorithm = get_object_or_404(Algorithm, friendly_title = friendly_title)
    current_user_likes = None
    if request.user in algorithm.likes.all():
        algorithm.likes.remove(request.user
        current_user_likes = 'Like'
    else:
        algorithm.likes.add(request.user)
        current_user_likes = 'Unlike'
    items = { 'likes': str(algorithm.likes.all().count()), 'current_user_likes': str(current_user_likes) }
    return JsonResponse(items)

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