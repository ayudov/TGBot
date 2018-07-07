#from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений
from db import users_db # Импортируем базу данных
import telebot
import config
from telebot import types
import gspread


#Подключение Google drive
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('TGTest').sheet1

#md = sheet.get_all_records()

#sheet.append_row(['111', '222'])
#----------


#Настройка бота
bot = telebot.TeleBot(config.TOKEN)
print(bot.get_me())
#----------

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)


@bot.message_handler(commands=['start'])  # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Помощь', 'Добавить себя', 'Получить ссылку')

    bot.send_message(message.chat.id, HELLO_MESSAGE, reply_markup=user_markup)


@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_messages(message):
    user_markup_back = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup_back.row('Главное меню')
    if message.text == 'Тополиный пух' or message.text == 'тополиный пух':
        bot.send_message(message.chat.id, ANSWER, reply_markup=user_markup_back)
    elif message.text == "Получить ссылку":
        bot.send_message(message.chat.id, URL_MESSAGE, reply_markup=user_markup_back)
    elif message.text == "Помощь":
        bot.send_message(message.chat.id,HELP_MESSAGE, reply_markup=user_markup_back)
    elif message.text == "Добавить себя":
        sheet.append_row([str(message.chat.id), str(message.from_user.id), str(message.from_user.first_name), str(message.from_user.last_name), str(message.from_user.username)])
        bot.send_message(message.chat.id, 'Ваша информация была добавлена', reply_markup=user_markup_back)
    elif message.text == "Главное меню":
        bot.send_message(message.from_user.id, 'Для начала работы напишите /start@AndreysTelegram666_bot')
    else:
        bot.send_message(message.chat.id, ELSE_ANSWER, reply_markup=user_markup_back)


if __name__ == '__main__':
    bot.polling(none_stop=True)