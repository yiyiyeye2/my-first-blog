from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
		# To save an object back to the database

	def __str__(self):
		return self.title
		# Double-check that you use two underscore characters (_) on each side of str. This convention is used frequently in Python and sometimes we also call them "dunder" (short for "double-underscore").

