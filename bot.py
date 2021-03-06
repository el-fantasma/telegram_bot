from glob import glob
from random import choice

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from utils import get_keyboard, get_user_emo

import settings

# Отчет о работе бота
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log'
	)


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


# Функция, которая соединяется с платформой Telegram
def main():
	bot = Bot(token=settings.TG_TOKEN, base_url=settings.TG_API_URL)
	mybot = Updater(bot = bot)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))       # Вызов функции greet_user при вызове команды /start
	dp.add_handler(CommandHandler("cat", send_cat, pass_user_data=True))

	dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat, pass_user_data=True))
	dp.add_handler(MessageHandler(Filters.regex('^(Изменить смайл-аватарку)$'), replace_user_emo, pass_user_data=True))
	dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
	dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))

	dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))  

	mybot.start_polling()
	mybot.idle()


if __name__ == "__main__":
	main()