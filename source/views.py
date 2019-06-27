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
from source.utils import GenericWebhooks, GenericAPIMethods, bot

from source.serializers import UserSerializers
from userprofile.models import UserProfile


headers = {
		'type': 'application/x-www-form-urlencoded',
		'token': settings.TELEGRAM_EMORY_BOT_HTTP_API,
	}


class UserData(GenericAPIMethods):

	def get_user(self, tel_id=None, **kwargs):
		try:
			if tel_id:
				user = UserProfile.objects.get(tel_id=tel_id)
			else:
				user = UserProfile.objects.get(tel_id=kwargs["tel_id"])
		except Exception as exc:
			try:
				user = UserProfile.objects.get(username=kwargs["username"])
			except Exception as exc:
				print("Can't get user!")

				return None

		return user


	def save_user_photo(self, user_id):

		url = self.upload_photo(user_id)
		print(url)
		user = self.get_user(user_id)
		user.image = url
		user.save()


	def get_user_data_message(self, user):
		message = """Данные о пользователе:\n 
		Имя: {}\n
		Фамилия: {}\n
		Город: {}\n
		Вид дейтельности: {}\n
		""".format(user.first_name, user.last_name, user.city, user.occupation)

		return message



class GenaricAPIViews(UserData, APIView):

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
		#path = self.upload_photo(369657072)

		return Response(responses)


class WebhooksView(UserData, APIView):

	#@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		#self.get_updates(self, *args, **kwargs)
		data = json.loads(self.request.body)
		chat = data["message"]["from"]
		chat.update({"tel_id": chat["id"]})
		serializer = UserSerializers(data=chat)
		if data["message"]["text"] == "/start" and serializer.is_valid():
			serializer.save()
			self.start(chat['id'])
		else:
			message = data["message"]["text"].lstrip()
			print
			user = self.get_user(**chat)
			if message.startswith("Вид дейтельности:"):
				self.save_user_occupation(user, message)
			elif message.startswith("Город:"):
				self.save_user_city(user, message)
			elif message.startswith("Посмотреть данные о себе"):
				self.get_user_data(user)
			else:
				self.error_message(user)
				#user = UserProfile.objects.get()
			#self.send_text_webhook(chat, data["message"]["text"])
		return super().dispatch(request, *args, **kwargs)

	def start(self, user_id):
		self.save_user_photo(user_id)
		#bot.send_message()

	def error_message(self, user):
		pass

	def save_user_city(self, user, message):
		user.city = message.split(":")[1].lstrip()
		user.save()

		response = bot.send_message(user.tel_id, "Ваш город сохранен", reply_markup=GenericWebhooks().main_manu())

	def save_user_occupation(self, user, message):
		user.occupation = message.split(":")[1].lstrip()
		user.save()
		
		response = bot.send_message(user.tel_id, "Ваш вид дейтельности сохранен", reply_markup=GenericWebhooks().main_manu())
		#image_path = self.upload_photo(user_id)
		#user = UserProfile.objects.get()

	def get_user_data(self, user):
		message = self.get_user_data_message(user)

		bot.send_message(user.tel_id, message, reply_markup=GenericWebhooks().main_manu())

	def loggin(self, request, *args, **kwargs):
		with open('loggin.txt', 'a') as file:
			file.write(json.dumps(request.data))

	def post(self, request, *args, **kwargs):
		#self.loggin(request, *args, **kwargs)
		#self.start(request, *args, **kwargs)
		return Response(status=status.HTTP_200_OK)
