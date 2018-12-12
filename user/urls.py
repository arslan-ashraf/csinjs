from django.conf.urls import url
from .views import user_login, create, update, delete, profile, change_password, logout

app_name = 'user'

urlpatterns = [
    url(r'^user/login/$', login, name = 'login'),
    url(r'^user/create/$', create, name = 'create'),
    url(r'^user/update/$', update, name = 'update'),
    url(r'^user/change-password/$', change_password, name = 'change_password'),
    url(r'^user/logout/$', logout, name = 'logout'),
	url(r'^user/profile/$', profile, name = 'profile'),
	url(r'^user/delete/$', delete, name = 'delete'),
]