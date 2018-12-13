from django.contrib import admin
from .models import Comment

class Comment_admin(admin.ModelAdmin):
	list_display = ['user', 'article', 'algorithm', 'content', 'created_at']
	class Meta:
		model = Comment

admin.site.register(Comment, Comment_admin)