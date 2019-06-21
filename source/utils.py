import requests
import json 
import telebot
import urllib.request

from django.shortcuts import render
from django.conf import settings
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from source.markups import MarkUps
from source.models import MenuCategories, GeneralInformation


headers = {
		'type': 'application/x-www-form-urlencoded',
		'token': settings.TELEGRAM_EMORY_BOT_HTTP_API,
	}


bot = telebot.TeleBot(settings.TELEGRAM_EMORY_BOT_HTTP_API)


class UserManager():
	""" User manager to get user data """

	def get_chat_id(self, request):
		return request.data['message']['chat']['id']

	def initail(self, *args, **kwargs):
		user = UserProfile.objects.create()


class GenericAPIMethods():
	""" generic API methods for initialize this bot """   
	
	def get_me(self, *args, **kwargs):
		response = requests.get(
				settings.TELEGRAM_EMORY_BOT_URL + "bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API + 
					"/getMe"
			)
		#response = requests.post(url)
		print(response.text)

	def get_updates(self, *args, **kwargs):

		response = requests.post(
			settings.TELEGRAM_EMORY_BOT_URL + "bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API + 
					"/getUpdates",
			)

		print(response.text)

	def set_webhook_url(self, *args, **kwargs):
		url = 'https://d4613b86.ngrok.io/source/webhooks/'

		response = requests.post(
			settings.TELEGRAM_EMORY_BOT_URL + "bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API + 
					"/setWebHook?url=" + url,
			)

		print(response.text)

	def webhook_info(self, *args, **kwargs):
		response = requests.post(
			settings.TELEGRAM_EMORY_BOT_URL + "bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API + 
					"/getWebhookInfo",
			)

		print(response.text)

	def send_message(self, message, *args, **kwargs):
		#message = "Test message"

		response = requests.post(
			settings.TELEGRAM_EMORY_BOT_URL + "bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API + 
					"/sendMessage",
			data={
					'chat_id': 369657072,
					'text': message
				}
			)

		print(response.text)

	def upload_photo(self, user_id):

		response = requests.post(
			settings.TELEGRAM_EMORY_BOT_URL + "bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API + 
					"/getUserProfilePhotos",
			data={
					'user_id': 369657072,
				}
			)

		print(json.loads(response.text)['result']['photos'][0][0]['file_id'])
		file_id = json.loads(response.text)['result']['photos'][0][0]['file_id']

		response = requests.post(
			settings.TELEGRAM_EMORY_BOT_URL + "bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API + 
					"/getFile",
			data={
					'file_id': file_id,
				}
			)

		file_path = json.loads(response.text)["result"]["file_path"]

		path = settings.MEDIA_ROOT + 'users/' + str(user_id) + '.jpg'

		urllib.request.urlretrieve(
			settings.TELEGRAM_EMORY_BOT_URL + "file/bot" +
					settings.TELEGRAM_EMORY_BOT_HTTP_API +
					'/' + file_path,
			path
			)

		return path





class GenericWebhooks(MarkUps): 
	""" generic webhooks methods to get response for each user request """

	def send_text_webhook(self, chat, text):

		gen_inf = GeneralInformation.objects.filter(title=text) 

		if gen_inf:
			message = gen_inf.last().text
		else:
			message = "Выберите пункт из меню"
		
		bot.send_message(chat["id"], message, reply_markup=self.main_manu())


	def send_main_manu_webhook(self, message):
		
		message = "Hi, I am an Emory bot"
		json_data = {
	        "chat_id": kwargs["chat_id"],
	        "text": kwargs["message"],
	    }
		response = requests.post(
			settings.TELEGRAM_EMORY_BOT_URL + "bot" +
				settings.TELEGRAM_EMORY_BOT_HTTP_API + 
				"/sendMessage",
			data= json_data
		)


	def send_image_webhook(self, request, *args, **kwargs):
		pass

	#def start(self, *args, **kwargs):


	# def users_list(self, request, *args, **kwargs):

	# 	message = "List of all users:"

	# 	json_data = 


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
