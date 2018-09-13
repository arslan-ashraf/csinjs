from django.contrib import admin
from .models import Algorithm

class Algorithm_admin(admin.ModelAdmin):
	list_display = ['title', 'friendly_title', 'category', 'code', 'created_at', 'updated_at']
	class Meta:
		model = Algorithm


admin.site.register(Algorithm, Algorithm_admin)