from django.db import models

# Create your models here.
from shortener.models import yellowURL

class ClickEventManager(models.Manager):
	def create_event(self,yellowinstance):
		if isinstance(yellowinstance,yellowURL):
			obj,created=self.get_or_create(yellow_url=yellowinstance)
			obj.count+=1
			obj.save()
			return obj.count
		return None


class ClickEvent(models.Model):
	yellow_url=models.OneToOneField(yellowURL)
	count=models.IntegerField(default=0)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects=ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)
