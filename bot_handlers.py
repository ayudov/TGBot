from bot import bot # Импортируем объект бота
from messages import * # Инмпортируем все с файла сообщений
from db import users_db # Импортируем базу данных


@bot.message_handler(commands=['start']) # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
        bot.send_message(message.chat.id, HELLO_MESSAGE)
#    # Если пользователя нет в базе
#    if not users_db.find_one({"chat_id": message.chat.id}):
#        users_db.insert_one({"chat_id" : message.chat.id})
#        bot.send_message(message.chat.id, HELLO_MESSAGE)
#    # Если пользователь есть в базе
#    else:
#        bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)


@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_messages(message):
    if message.text == 'Тополиный пух':
        bot.send_message(message.chat.id, ANSWER)
    else:
        bot.send_message(message.chat.id, "блаблабла(я пишу только одно сообщение)\nНаисано @ AndreyYudov(https://t.me/AndreyYudov)\n(Хочешь прикол - напиши 'Тополиный пух'")


if __name__ == '__main__':
    bot.polling(none_stop=True)