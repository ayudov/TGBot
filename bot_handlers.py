#from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений
from db import users_db # Импортируем базу данных
import telebot
import config
from telebot import types


#Настройка бота
bot = telebot.TeleBot(config.TOKEN)
print(bot.get_me())
#----------

@bot.message_handler(commands=['help'])
def send_help(message):
        bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(commands=['start']) # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Помощь', 'Получить ссылку на Google spreadsheet')

    bot.send_message(message.chat.id, HELLO_MESSAGE, reply_markup=user_markup)

@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_messages(message):
    if message.text == 'Тополиный пух' or message.text == 'тополиный пух':
        bot.send_message(message.chat.id, ANSWER)
    elif message.text == "Получить ссылку на Google spreadsheet":
        bot.send_message(message.chat.id, URL_MESSAGE)
    elif message.text == "Помощь":
        bot.send_message(message.chat.id,HELP_MESSAGE)



if __name__ == '__main__':
    bot.polling(none_stop=True)