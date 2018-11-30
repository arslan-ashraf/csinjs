from django.conf.urls import url
from .views import blogs_home, create, edit, delete

app_name = 'blog'

urlpatterns = [
    url(r'^blogs/$', blogs_home, name = 'blogs_home'),
    url(r'^blog/(?P<friendly_title>[-\w]+)/$', show, name = 'title'),
	url(r'^blog/(?P<friendly_title>[-\w]+)/edit/$', update, name = 'update'),
	url(r'^blog/(?P<friendly_title>[-\w]+)/delete/$', delete, name = 'delete'),
    url(r'^blog/create/$', create, name = 'create'),
   
]