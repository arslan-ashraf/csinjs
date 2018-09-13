from django.db import models
from django.urls import reverse

# Create your models here.
class Algorithm(models.Model):
	title = models.CharField(max_length = 300)
	category = models.CharField(max_length = 300)
	code = models.TextField()
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('title', kwargs = {'title': self.title})