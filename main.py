from telebot import types
from telebot import TeleBot
import sqlite3
import telebot
from utils import messages
from utils import set_user_from_message
from utils import set_question_from_message

from dbase import create_tables


bot = TeleBot("5580320258:AAEYAMH3Gg_XZApHEi4hOgzk7uNqmszUDX8")
connect = sqlite3.connect('telebot.db', check_same_thread=False)
admin_id = 596459751


@bot.message_handler(commands=['start'])
def user_registration(message):                                #Connection with is database and create table

    # User registration

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = messages['question_btn_text']
    markup.add(item1)
    bot.send_message(message.chat.id, messages['start'], reply_markup=markup)

    set_user_from_message(message, connect)


@bot.message_handler(regexp=messages['question_btn_text'])
def preparing_for_question(message):
    if message.text == messages['question_btn_text']:
        bot.send_message(message.from_user.id, messages['get_question'])
        bot.register_next_step_handler(message, register_question)


def register_question(message):
    if message.text == messages['question_btn_text']:
        bot.send_message(message.from_user.id, messages['get_question'])
        bot.register_next_step_handler(message, register_question)
        return
    question_id = set_question_from_message(message, connect)

    bot.send_message(message.from_user.id, messages['success'])
    send_to_admin(question_id, message)


def send_to_admin(question_id, message):
    button_approve = types.InlineKeyboardButton('approve', callback_data='approve')
    button_disapprove = types.InlineKeyboardButton('disapprove', callback_data='disapprove')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_approve)
    keyboard.add(button_disapprove)
    bot.send_message(admin_id, messages['new_question'].format(message.from_user.username))
    text = f'{question_id}. {message.text}'
    message = bot.send_message(admin_id, text=text, reply_markup=keyboard)
    return message


if __name__ == '__main__':
    create_tables(connect)
    bot.polling(none_stop=True)
