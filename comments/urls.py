from django.conf.urls import url
from .views import send_comment

app_name = 'comments'

urlpatterns = [
    url(r'^send_comment/$', send_comment, name = 'send_comment'),
]