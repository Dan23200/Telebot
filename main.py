from telebot import types
import telebot
import sqlite3
from utils import messages

bot = telebot.TeleBot("5580320258:AAEYAMH3Gg_XZApHEi4hOgzk7uNqmszUDX8")


@bot.message_handler(commands=['start'])
def user_registration(message):                                #Connection with is database and create table

    # User registration

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = messages['question_btn_text']
    markup.add(item1)
    bot.send_message(message.chat.id, messages['start'], reply_markup=markup)
    print('Кнопки работают')
    bot.register_next_step_handler(message, register_question)


def register_question(message):
    if message.text == messages['question_btn_text']:
        bot.send_message(message.from_user.id, messages['get_question'])


if name == '__main__':
    create_tables(connect)
    bot.polling(none_stop=True)