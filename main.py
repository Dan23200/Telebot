from telebot import types
import telebot
from datetime import datetime
import sqlite3
from utils import messages
from utils import database_dict
from dbase import create_tables
from dbase import QuestionDB


bot = telebot.TeleBot("5580320258:AAEYAMH3Gg_XZApHEi4hOgzk7uNqmszUDX8")
connect = sqlite3.connect('telebot.db')


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
        bot.register_next_step_handler(message, register_information)


def register_information(message):
    reformat_date = datetime.now().strftime("%d.%m.%G %H:%M:%S")
    c_date, c_time = reformat_date.split()
    message_datetime = f"{database_dict['date_message']}: {c_date}\n{database_dict['time_message']}: {c_time}"


    # while True:
    #     if message.text == messages['question_btn_text']:
    #         bot.send_message(message.from_user.id, messages['get_question'])
    #         break
    #     elif message.text != messages['question_btn_text']:
    #         break

    question_db = QuestionDB(db)

    question = {
        'id': None,
        'user_id': message.chat.id,
        'user_name': message.from_user.first_name,
        'user_last_name': message.from_user.last_name,
        'date': message_datetime,
        'question': message.text
    }
    
    question_db.set
    print(question['id'])
    print(message.chat.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message_datetime)
    print(message.text)



# @bot.message_handler()
# def finish_answering:
#     if
#




if __name__ == '__main__':
    create_tables(connect)
    bot.polling(none_stop=True)
