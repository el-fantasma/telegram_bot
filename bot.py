from telegram import Bot

from telegram.ext import Updater                   # Обработчик запросов
from telegram.ext import CommandHandler            # Обработчик команд
from telegram.ext import MessageHandler, Filters   # Обработчик текстовых сщщбщений


# Отчет о работе бота
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log'
	)


TG_TOKEN = "1075912832:AAF1n7hjFG4h7i1PFMhZUhSBTccvfXZCNTI"
TG_API_URL = "https://telegg.ru/orig/bot"


# Функция, которая соединяется с платформой Telegram
def main():
	bot = Bot(token=TG_TOKEN, base_url=TG_API_URL)
	mybot = Updater(bot = bot)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))       # Вызов функции greet_user при вызове команды /start
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # Вызов функции для ответа пользователю

	mybot.start_polling()
	mybot.idle()


def greet_user(bot, update):
	text = 'Вызван /start'
	print(text)
	update.message.reply_text(text)


def talk_to_me(bot, update):
	user_text = update.message.text
	print(user_text)
	update.message.reply_text(user_text)

main()