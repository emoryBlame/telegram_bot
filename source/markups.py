from telebot import types

from source.models import MenuCategories, GeneralInformation 
#from utils import bot


class MarkUps():
	""" Make menu's optionality """

	def main_manu(self):
		markup = types.ReplyKeyboardMarkup(row_width=2)
		category = MenuCategories.objects.get(title="Основное")
		items = GeneralInformation.objects.filter(contain__id=category.id)
		itembtns = [types.KeyboardButton(item.title) for item in items]
		markup.add(*itembtns)

		return markup

	def choicen_menu(self, cat_title):
		markup = types.ReplyKeyboardMarkup(row_width=2)
		category = MenuCategories.objects.get(title=cat_title)
		if not category:
			category = MenuCategories.objects.get(title="Основное")
		items = GeneralInformation.objects.filter(contain__id=category.id)
		itembtns = [types.KeyboardButton(item.title) for item in items]
		markup.add(*itembtns)

		return markup