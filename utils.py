from emoji import emojize

from random import choice

from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton

import settings

def get_user_emo(user_data):
	if 'emo' in user_data:
		return user_data['emo']
	else:
		user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
		return user_data['emo']

def get_keyboard():
	contact_button = KeyboardButton('Контактные данные', request_contact=True)
	location_button = KeyboardButton('Геолокация', request_location=True)
	my_keyboard = ReplyKeyboardMarkup([
		['Прислать котика', 'Изменить смайл-аватарку'],
		[contact_button, location_button]
		], resize_keyboard=True)
	return my_keyboard
