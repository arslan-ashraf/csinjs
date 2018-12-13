from django.conf.urls import url
from .views import user_login, create, update, delete, profile, change_password, user_logout
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
	url(r'^user/login/$', user_login, name = 'user_login'),
    url(r'^user/create/$', create, name = 'create'),
    url(r'^user/update/$', update, name = 'update'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'home.html')),
    url(r'^user/change-password/$', change_password, name = 'change_password'),
	url(r'^user/profile/$', profile, name = 'profile'),
	url(r'^user/delete/$', delete, name = 'delete'),
]