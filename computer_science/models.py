from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User

class Algorithm(models.Model):
	title = models.CharField(max_length = 300)
	friendly_title = models.SlugField(unique = False, default = None)
	category = models.CharField(max_length = 300, default = None)
	friendly_category = models.SlugField(unique = False, default = None)
	code = models.TextField()
	likes = models.ManyToManyField(User, blank = True, related_name = 'algorithm_likes')
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('computer_science:title', kwargs = {
						'friendly_category': self.friendly_category,
						'friendly_title': self.friendly_title}
						)

	def get_category_url(self):
		return reverse('computer_science:index', kwargs = { 'friendly_category': self.friendly_category })

	class Meta:
		ordering = ['title']


def create_friendly_title(sender, instance, *args, **kwargs):
	friendly_title = slugify(instance.title)
	friendly_category = slugify(instance.category)
	instance.friendly_title = friendly_title
	instance.friendly_category = friendly_category


pre_save.connect(create_friendly_title, sender = Algorithm)