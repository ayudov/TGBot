from bot import bot # Импортируем объект бота
from bot import user_markup
from messages import * # Инмпортируем все с файла сообщений
from db import users_db # Импортируем базу данных
from telebot import types
#import bot

@bot.message_handler(commands=['help'])
def send_help(message):
        bot.send_message(message.chat.id, HELP_MESSAGE)

@bot.message_handler(commands=['start']) # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
        user_markup.row('Помощь', 'Получить ссылку на Google spreadsheet')

        bot.send_message(message.chat.id, HELLO_MESSAGE, reply_markup=user_markup)

        '''key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Android", callback_data="Android pressed")
        but_2 = types.InlineKeyboardButton(text="IOS", callback_data="IOS pressed")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "What is your OS?", reply_markup=key)'''


'''    # Если пользователя нет в базе
    if not users_db.find_one({"chat_id": message.chat.id}):
        users_db.insert_one({"chat_id" : message.chat.id})
        bot.send_message(message.chat.id, HELLO_MESSAGE)
    # Если пользователь есть в базе
    else:
        bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)'''



@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_messages(message):
    if message.text == 'Тополиный пух' or message.text == 'тополиный пух':
        bot.send_message(message.chat.id, ANSWER)
    elif message.text == "Получить ссылку на Google spreadsheet":
        bot.send_message(message.chat.id, URL_MESSAGE)
    else:
        bot.send_message(message.chat.id,ELSE_ANSWER)



if __name__ == '__main__':
    bot.polling(none_stop=True)