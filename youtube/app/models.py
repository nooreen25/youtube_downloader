from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
	link=models.URLField(max_length=200)

	def __unicode__(self):
		return self.link
