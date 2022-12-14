from datetime import datetime
from dbase import UserDB
from dbase import QuestionDB


messages = {
    'start': 'Приветсвую! Я бот, который собирает вопросы для чата',
    'get_question': 'Напишите свой вопрос',
    'question_btn_text': 'Оставить вопрос',
    'success': 'Готово! Ваш вопрос успешно сохранен!',
    'new_question': 'Новый вопрос от пользователя @{}',
    'approve_admin': 'Вы одобрили вопрос, сообщение о вашем одобрение прийдет пользователю',
    'disapprove_admin': 'Вы НЕ одобрили вопрос, сообщение о вашем НЕ одобрение прийдет пользователю',
    'approve_user': 'Администратор одобрил ваш вопрос ',
    'disapprove_user': 'Администратор НЕ одобрил ваш вопрос '
}

database_dict = {
    'date_message': 'Дата получения сообщения',
    'time_message': 'Время получения сообщения'
}


def set_user_from_message(message, connect):
    user = {
        'user_id': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'message_date': datetime.now(),
    }
    user_db = UserDB(connect)
    user_db.set_user(user)


def set_question_from_message(message, connect):
    question = {
        "id": None,
        "user_id": message.from_user.id,
        "question": message.text,
        "message_date": datetime.now(),
    }
    user_db = QuestionDB(connect)
    user_db.add_question(question)
    question_id = user_db.get_question_id_by_info(question)
    return question_id
