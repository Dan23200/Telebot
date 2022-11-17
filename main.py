from telebot import types
import telebot
import sqlite3
from utils import messages

bot = telebot.TeleBot("5580320258:AAEYAMH3Gg_XZApHEi4hOgzk7uNqmszUDX8")


@bot.message_handler(commands=['start'])
def user_registration(message):                                #Connection with is database and create table
    connect = sqlite3.connect('telebot.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS question(
        users_id INTEGER PRIMARY KEY,
        question TEXT,
        date DATETIME
    )""")
    connect.commit()

    question = {
        'user_id': message.from_user_id,
        'question': message.text,
        'date': None
    }

    # User registration

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = messages['question_btn_text']
    markup.add(item1)
    bot.send_message(message.chat.id, messages['start', 'get_question'], reply_markup=markup)
    print('Кнопки работают')


bot.polling(none_stop=True)
#
# people_id = message.chat.id
# cursor.execute(f"SELECT users_id FROM question WHERE users_id = {people_id}")
# data = cursor.fetchone()
# if data is None:
#     users_id = [message.chat.id]
#     cursor.execute("INSERT INTO question VALUES(?, ?, ?);", users_id, )
#     connect.commit()
# else:
#     bot.send_message(message.chat.id, '{0.first_name}, рад тебя видеть вновь 😁'.format(message.from_user))




