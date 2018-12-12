from django.conf.urls import url
from .views import login, create, update, delete, profile

app_name = 'user'

urlpatterns = [
    url(r'^user/login/$', login, name = 'login'),
    url(r'^user/create/$', create, name = 'create'),
    url(r'^user/update/$', update, name = 'update'),
	url(r'^user/profile/$', profile, name = 'profile'),
	url(r'^user/delete/$', delete, name = 'delete'),
]