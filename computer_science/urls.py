from django.conf.urls import url
from .views import home, categories, show

app_name = 'computer_science'

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^categories/$', categories, name = 'categories'),
    url(r'^title/(?P<title>[-\w]+)/$', show, name = 'title'),
    # url(r'^$', home, name = 'home'),
]