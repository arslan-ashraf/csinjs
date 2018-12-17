from django.conf.urls import url
from .views import delete_notification

app_name = 'comment'

urlpatterns = [
    url(r'^delete-notification/(?P<notification_id>\d+)/$', delete_notification, name = 'delete_notification'),
]