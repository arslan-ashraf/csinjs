from django.conf.urls import url
from .views import blogs_home

app_name = 'blog'

urlpatterns = [
    url(r'^blogs/$', blogs_home, name = 'blogs_home'),
 #    url(r'^algorithms/(?P<friendly_category>[-\w]+)/$', index, name = 'index'),
 #    url(r'^algorithms/$', categories, name = 'categories'),
 #    url(r'^algorithms/(?P<friendly_category>[-\w]+)/(?P<friendly_title>[-\w]+)/$', show, name = 'title'),
	# url(r'^algorithms/(?P<friendly_category>[-\w]+)/(?P<friendly_title>[-\w]+)/edit/$', update, name = 'update'),
	# url(r'^algorithms/(?P<friendly_category>[-\w]+)/(?P<friendly_title>[-\w]+)/delete/$', delete, name = 'delete'),
 #    url(r'^algorithm/create/$', create, name = 'create'),
   
]