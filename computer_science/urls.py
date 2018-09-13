from django.conf.urls import url
from .views import home, categories, show, create, update, delete

app_name = 'computer_science'

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^algorithms/categories/$', categories, name = 'categories'),
    url(r'^algorithms/(?P<friendly_title>[-\w]+)/$', show, name = 'title'),
	url(r'^algorithms/(?P<friendly_title>[-\w]+)/edit/$', update, name = 'update'),
    url(r'^algorithms/create/$', create, name = 'create'),
    url(r'^algorithms/delete/$', delete, name = 'delete'),
]