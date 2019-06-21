import requests

from django.views.generic import View
from django.conf import settings

from rest_framework import serializers

from userprofile.models import UserProfile


class UserSerializers(serializers.ModelSerializer):
	""" serialize UserProfile model and some additional methods"""

	#type = CharField(max_length=20)

	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'username')#, 'phone')


class UserPhotoSerializers(serializers.ModelSerializer):
	""" serialize UserProfile model and some additional methods"""

	#type = CharField(max_length=20)

	class Meta:
		model = UserProfile
		fields = ('photo', 'username')#, 'phone')



