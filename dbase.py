class QuestionDB:
    def __init__(self, db):
        self.db = db

    def add_information(self, question):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO users (id, user_id, user_name, user_last_name, date,) VALUES (?, ?, ?, ?, ?)",
            (question['id'], question['user_id'], question['user_name'], question['user_last_name'], question['message_date'])
        )
        self.db.commit()

    def add_question(self, question):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO question (id, user_id, question, date,) VALUES (?, ?, ?, ?)",
            (question['id'], question['user_id'], question['question'], question['date'])
        )
        self.db.commit()


class DataBase:
    def __init__(self, db):
        self.db = db


def create_tables(db):
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        "id" INTEGER PRIMARY KEY,
                        "user_id" INTEGER,
                        "user_name" CHAR(40),
                        "user_last_name" CHAR(40),
                        "message_date" TEXT
                        FOREIGN KEY ("user_id")  REFERENCES question ("user_id")
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS question (
                        "id" INTEGER PRIMARY KEY,
                        "user_id" INTEGER,
                        "question" TEXT,
                        "message_date" TEXT
                    )''')

    db.commit()
