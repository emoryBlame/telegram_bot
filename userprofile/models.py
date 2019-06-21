from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(User):
	tel_id = models.CharField(max_length=100) 
	#username = models.CharField(max_length=100, blank=True) 
	phone = models.CharField(max_length=100, blank=True) 
	city = models.CharField(max_length=50)
	occupation = models.CharField(max_length=1000, blank=True)
	description = models.TextField(max_length=5000, blank=True)
	image = models.ImageField(upload_to='users/', blank=True, max_length=100)
	

	def __str__(self):
		return self.username
