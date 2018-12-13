from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog
from computer_science.models import Algorithm

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	article = models.ForeignKey(Blog, on_delete = models.CASCADE, null = True, blank = True)
	algorithm = models.ForeignKey(Algorithm, on_delete = models.CASCADE, null = True, blank = True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.user.username)