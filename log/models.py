from django.db import models

# Create your models here.
class logPeople(models.Model):
	name = models.CharField(max_length=50)
	position = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

