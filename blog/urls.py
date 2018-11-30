from django.conf.urls import url
from .views import blogs_home, create, update, delete, show

app_name = 'blog'

urlpatterns = [
    url(r'^blogs/$', blogs_home, name = 'blogs_home'),
    url(r'^blog/(?P<friendly_title>[-\w]+)/$', show, name = 'show'),
	url(r'^blog/(?P<friendly_title>[-\w]+)/update/$', update, name = 'update'),
	url(r'^blog/(?P<friendly_title>[-\w]+)/delete/$', delete, name = 'delete'),
    url(r'^blog/create/$', create, name = 'create'),
   
]