from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Blog
from .forms import Blog_form
from comments.forms import Comment_form
from django.contrib.auth.decorators import login_required
from comments.models import Comment, Notification

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
	if (request.method == 'POST'):
	    new_comment = Comment.objects.create(user = request.user, blog = blog, content = request.POST['typed_comment'])
	    for each_user in algorithm.users.all():
	        if each_user == request.user:
	            continue
	        Notification.objects.create(sender = request.user.username, receiver = each_user.username, action = 'posted a', body = 'comment', url = blog.get_absolute_url())
	    blog.users.add(request.user)
	    return render(request, 'comments/new_comment.html', { 'comment': new_comment })
	form = Comment_form(request.POST or None)
	current_user_likes = False
	like_or_unlike = 'Like'
	if request.user.is_authenticated:
	    if request.user in blog.likes.all():
	        current_user_likes = True
	    if current_user_likes:
	        like_or_unlike = 'Unlike'
	items = { 'blog': blog[0],
	          'title': blog[0].title,
	          'comments': blog[0].comment_set.all(),
	          'form': form,
	          'value': 'Submit Comment',
	          'like_or_unlike': like_or_unlike,}
	# print('#' * 50)
	# print(Blog[0])
	# print('#' * 50)
	return render(request, 'blogs/blog_show.html', items)

@login_required
def blog_like(request, friendly_title = None):
    blog = get_object_or_404(Blog, friendly_title = friendly_title)
    current_user_likes = None
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
        current_user_likes = 'Like'
    else:
        blog.likes.add(request.user)
        current_user_likes = 'Unlike'
    items = { 'likes': str(blog.likes.all().count()), 'current_user_likes': str(current_user_likes) }
    return JsonResponse(items)

def delete(request, friendly_title = None):
	if not request.user.is_superuser:
		return Http404
	blog = Blog.objects.filter(friendly_title = friendly_title)
	if not blog:
		return Http404
	blog.delete()
	return redirect("computer_science:home", permanent = True)