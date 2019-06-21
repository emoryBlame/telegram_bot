import requests
import json 
import telebot

from django.shortcuts import render
from django.conf import settings
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from source.utils import GenericWebhooks, GenericAPIMethods

from source.serializers import UserSerializers
from userprofile.models import UserProfile


headers = {
		'type': 'application/x-www-form-urlencoded',
		'token': settings.TELEGRAM_EMORY_BOT_HTTP_API,
	}


class GenaricAPIViews(GenericAPIMethods, APIView):

	def dispatch(self, request, *args, **kwargs):
		#self.get_updates(self, *args, **kwargs)
		#self.set_webhook_url(self, *args, **kwargs)
		return super().dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		responses = {}
		#self.get_me(*args, **kwargs)
		#self.get_updates(*args, **kwargs)
		#self.webhook_info(*args, **kwargs)
		#self.set_webhook_url(*args, **kwargs)
		#self.send_message("message", *args, **kwargs)
		path = self.upload_photo(369657072)

		return Response(responses)

	def get_user_data(self, user_id):

		self.upload_photo(user_id)



class WebhooksView(GenericWebhooks, APIView):

	#@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		#self.get_updates(self, *args, **kwargs)
		data = json.loads(self.request.body)
		print(data)
		chat = data["from"]["id"]
		serializer = UserSerializers(data=chat)
		if data["message"]["text"] == "/start" and serializer.is_valid():
			serializer.save()
			self.start(chat['id'])
		#self.send_text_webhook(chat, data["message"]["text"])
		return super().dispatch(request, *args, **kwargs)

	def start(user_id):
		self.get_user_data(user_id)

	def get_user_data(self, user_id):

		image_path = self.upload_photo(user_id)
		#user = UserProfile.objects.get()


	def loggin(self, request, *args, **kwargs):
		with open('loggin.txt', 'a') as file:
			file.write(json.dumps(request.data))

	def post(self, request, *args, **kwargs):
		#self.loggin(request, *args, **kwargs)
		#self.start(request, *args, **kwargs)
		return Response(status=status.HTTP_200_OK)
