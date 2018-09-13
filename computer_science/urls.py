from django.conf.urls import url
from .views import home

app_name = 'computer_science'

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^categories/$', categories, name = 'categories'),
    url(r'^title/$', show, name = 'title'),
    # url(r'^$', home, name = 'home'),
]
