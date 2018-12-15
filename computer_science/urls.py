from django.conf.urls import url
from .views import home, categories, show, create, update, delete, search, index

app_name = 'computer_science'

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^algorithms/search/$', search, name = 'search'),
    url(r'^algorithms/(?P<friendly_category>[-\w]+)/$', index, name = 'index'),
    url(r'^algorithms/$', categories, name = 'categories'),
    url(r'^algorithms/(?P<friendly_category>[-\w]+)/(?P<friendly_title>[-\w]+)/$', show, name = 'title'),
	url(r'^algorithms/(?P<friendly_category>[-\w]+)/(?P<friendly_title>[-\w]+)/edit/$', update, name = 'update'),
	url(r'^algorithms/(?P<friendly_category>[-\w]+)/(?P<friendly_title>[-\w]+)/delete/$', delete, name = 'delete'),
    url(r'^algorithm/create/$', create, name = 'create'),

]