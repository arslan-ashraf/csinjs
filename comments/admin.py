from django.contrib import admin
from .models import Comment, Notification

class Comment_admin(admin.ModelAdmin):
	list_display = ['user', 'article', 'algorithm', 'content', 'created_at']
	class Meta:
		model = Comment

class Notification_admin(admin.ModelAdmin):
	list_display = ['sender', 'receiver', 'action', 'body', 'url']
	class Meta:
		model = Notification

admin.site.register(Comment, Comment_admin)
admin.site.register(Notification, Notification_admin)