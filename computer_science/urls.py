from django.conf.urls import url
from .views import home, categories, show, create

app_name = 'computer_science'

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^categories/$', categories, name = 'categories'),
    url(r'^algorithm/title/(?P<friendly_title>[-\w]+)/$', show, name = 'title'),
    url(r'^create/$', create, name = 'create'),
]