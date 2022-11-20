
class BaseDB:
    def __init__(self, db):
        self. db = db


class QuestionDB(BaseDB):
    def add_question(self, question):
        cursor = self.db.cursor()
        cursor.execute(
            'INSERT INTO question (id, user_id, question, message_date) VALUES (?, ?, ?, ?)',
            (question['id'], question['user_id'], question['question'], question['message_date'])
        )
        self.db.commit()


class UserDB(BaseDB):
    def set_user(self, user):
        cursor = self.db.cursor()
        cursor.execute(
            """INSERT INTO user (user_id, username, first_name, last_name, message_date) 
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT (user_id)
                DO UPDATE SET
                username = (?),
                first_name = (?),
                last_name = (?),
                message_date = (?);
            """,
            (user['user_id'], user['username'], user['first_name'], user['last_name'], user['message_date'], user['username'], user['first_name'], user['last_name'], user['message_date'])
        )
        self.db.commit()


def create_tables(db):
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                        "user_id" INTEGER PRIMARY KEY,
                        "username" CHAR(40),
                        "first_name" CHAR(40),
                        "last_name" CHAR(40),
                        "message_date" DATATIME                       
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS question (
                        "id" INTEGER PRIMARY KEY,
                        "user_id" INTEGER,
                        "question" TEXT,
                        "message_date" DATETIME,
                        FOREIGN KEY ("user_id")  REFERENCES user ("user_id")
                    )''')

    db.commit()
