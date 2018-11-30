from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

<<<<<<< HEAD
# Create your models here.
=======
>>>>>>> 0448bf8ebcf94dba9f77cba8564c50d5b35cbf59
class Blog(models.Model):
	title = models.CharField(max_length = 300)
	friendly_title = models.SlugField(unique = False, default = None)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

<<<<<<< HEAD
	# def get_absolute_url(self):
	# 	return reverse('blog:title', kwargs = {
	# 					'friendly_title': self.friendly_title}
	# 					)
=======
	def get_absolute_url(self):
		return reverse('blog:show', kwargs = { 'friendly_title': self.friendly_title })
>>>>>>> 0448bf8ebcf94dba9f77cba8564c50d5b35cbf59

	class Meta:
		ordering = ['title']


def create_friendly_title(sender, instance, *args, **kwargs):
	friendly_title = slugify(instance.title)
	instance.friendly_title = friendly_title

pre_save.connect(create_friendly_title, sender = Blog)