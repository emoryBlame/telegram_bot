import requests

from django.views.generic import View
from django.conf import settings

from rest_framework import serializers

from userprofile.models import UserProfile


class UserSerializers(serializers.ModelSerializer):
	""" serialize UserProfile model and some additional methods"""

	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'username', 'tel_id')#, 'phone')

	# def save(self, **kwargs):
	# 	print(kwargs)
	# 	user = super().save(**kwargs)
	# 	user.tel_id = kwargs["id"]
	# 	user.save()
	# 	return user


class UserPhotoSerializers(serializers.ModelSerializer):
	""" serialize UserProfile model and some additional methods"""

	#type = CharField(max_length=20)

	class Meta:
		model = UserProfile
		fields = ('photo', 'username')#, 'phone')



