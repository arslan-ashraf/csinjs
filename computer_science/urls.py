from django.conf.urls import url
from .views import home

# app_name = 'computer_science'

urlpatterns = [
    url(r'^$', home),
]
