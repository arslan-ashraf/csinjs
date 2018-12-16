from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Blog
from .forms import Blog_form
from comments.forms import Comment_form

def blogs_home(request):
	blogs = Blog.objects.all()
	items = { 'blogs': blogs, 'title': 'Articles' }
	return render(request, 'blogs/blogs_home.html', items)

def create(request):
	print('()' * 50)
	print('create')
	print('()' * 50)
	if not request.user.is_superuser:
		return Http404
	form = Blog_form(request.POST or None, request.FILES or None)
	if form.is_valid():
		new_blog = form.save(commit = False)

		print(new_blog)
		new_blog.save()
		return redirect(new_blog,
						new_blog.get_absolute_url,
						permanent = True)
	items = { 'form': form, 'title': 'Create New Blog', 'value': 'Create' }
	return render(request, 'blogs/blog_form.html', items)

def update(request, friendly_title = None):
	# print('|' * 50)
	# print(request)
	# print('|' * 50)
	if not request.user.is_superuser:
		return Http404
	blog = get_object_or_404(Blog, friendly_title = friendly_title)
	form = Blog_form(request.POST or None, request.FILES or None, instance = blog)
	if form.is_valid():
		updated_blog = form.save(commit = False)
		updated_blog.save()
		return redirect(updated_blog,
						updated_blog.get_absolute_url,
						permanent = True)
		# print('x' * 50)
		# print(x)
		# print('x' * 50)
	items = { 'form': form, 'title': 'Update Blog', 'value': 'Update' }
	return render(request, 'blogs/blog_form.html', items)

def show(request, friendly_title = None):
	blog = Blog.objects.filter(friendly_title = friendly_title)
	if not Blog:
		return Http404
	form = Comment_form(request.POST or None)
	if form.is_valid():
	    new_comment = form.save(commit = False)
	    new_comment.user = request.user
	    new_comment.blog = blog
	    new_comment.save()
	    return redirect(algorithm, algorithm.get_absolute_url, permanent = True)
	items = { 'blog': blog[0],
	          'title': blog[0].title,
	          'comments': blog[0].comment_set.all(),
	          'form': form,
	          'value': 'Submit Comment', }
	# print('#' * 50)
	# print(Blog[0])
	# print('#' * 50)
	return render(request, 'blogs/blog_show.html', items)

def blog_like(request):
    return

def delete(request, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	blog = Blog.objects.filter(friendly_title = friendly_title)
	if not blog:
		return Http404
	blog.delete()
	return redirect("computer_science:home", permanent = True)