from django.db import models

# Create your models here.
from django.db import models
class Book(models.Model):
	title = models.CharField(max_length=20)
	author = models.CharField(max_length=20)
 
	def __str__(self):
		return self.title