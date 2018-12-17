from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from comments.models import Comment, Notification
from django.contrib.auth.decorators import login_required

@login_required
def delete_notification(request, notification_id):
    notification = Notification.objects.filter(id = notification_id)
    notification.delete()
    return JsonResponse([], safe = False)