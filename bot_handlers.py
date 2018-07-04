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

@bot.message_handler(commands=['start']) # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Помощь','Добавить себя', 'Получить ссылку')   ''', 'Найти всё по ID пользователя'''

    bot.send_message(message.chat.id, HELLO_MESSAGE, reply_markup=user_markup)

@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_messages(message):
    if message.text == 'Тополиный пух' or message.text == 'тополиный пух':
        bot.send_message(message.chat.id, ANSWER)
    elif message.text == "Получить ссылку":
        bot.send_message(message.chat.id, URL_MESSAGE)
    elif message.text == "Помощь":
        bot.send_message(message.chat.id,HELP_MESSAGE)
    elif message.text == "Добавить себя":
        sheet.append_row([str(message.chat.id), str(message.from_user.id), str(message.from_user.first_name), str(message.from_user.last_name), str(message.from_user.username)])
        bot.send_message(message.chat.id, 'Ваша информация была добавлена')
    else:
        bot.send_message(message.chat.id, ELSE_ANSWER)

    '''elif message.text == "Найти всё по ID пользователя":
        user_markup_find = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup_find.row('Главное меню')
        bot.send_message(message.chat.id, 'Пожалуйста, введите ID (9 символов)', reply_markup=user_markup_find)'''

        #bot.send_message(message.chat.id, 'Перешел в пункт поиска пользователей')

    '''elif message.text == "Главное меню":
        send_welcome(message)'''


if __name__ == '__main__':
    bot.polling(none_stop=True)