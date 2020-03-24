from glob import glob
from random import choice

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from utils import get_keyboard, get_user_emo

import logging



def greet_user(bot, update, user_data):
	emo = get_user_emo(user_data)
	user_data['emo'] = emo
	text = 'Привет {}'.format(emo)
	logging.info(text)
	
	update.message.reply_text(text, reply_markup=get_keyboard())


def talk_to_me(bot, update, user_data):
	emo = get_user_emo(user_data)
	user_text = "Привет {} {}! Ты написал: {}.".format(update.message.chat.first_name, user_data['emo'], update.message.text)
	logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
		update.message.chat.id, update.message.text)
	update.message.reply_text(user_text, reply_markup=get_keyboard())


def send_cat(bot, update, user_data):
	cat_list = glob('images/cat*.jp*g')
	cat_pics = choice(cat_list)
	bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pics, 'rb'), reply_markup=get_keyboard())

def get_contact(bot, update, user_data):
	print(update.message.contact)
	update.message.reply_text('Спасибо, {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

def get_location(bot, update, user_data):
	print(update.message.location)
	update.message.reply_text('Спасибо, {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

def replace_user_emo(bot, update, user_data):
	if 'emo' in user_data:
		del user_data['emo']
	emo = get_user_emo(user_data)
	update.message.reply_text('Готово: {}'.format(emo))
