from django.db import models

# Create your models here.

class MenuCategories(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title


class GeneralInformation(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=2000)
	contain = models.ManyToManyField(MenuCategories)

	def __str__(self):
		return self.title
