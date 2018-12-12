from django.contrib import admin
from .models import Blog

class Blog_admin(admin.ModelAdmin):
	list_display = ['title', 'friendly_title', 'content', 'created_at', 'updated_at']
	class Meta:
		model = Blog

admin.site.register(Blog, Blog_admin)