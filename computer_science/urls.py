from django.conf.urls import url
from .views import home, categories, show, create, update, delete

app_name = 'computer_science'

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^categories/$', categories, name = 'categories'),
    url(r'^title/(?P<friendly_title>[-\w]+)/$', show, name = 'title'),
	url(r'^title/(?P<friendly_title>[-\w]+)/edit/$', update, name = 'update'),
    url(r'^create/$', create, name = 'create'),
    url(r'^delete/$', delete, name = 'delete'),
]