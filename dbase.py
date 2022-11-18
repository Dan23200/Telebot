class QuestionDB:
    def __init__(self, db):
        self.db = db

    def set_question(self, question):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO question (user_id, question, date) VALUES (?, ?, ?)",
            (question['user_id'], question['question'], question['date'])
        )
        self.db.commit()
