############################################################
from app import db
############################################################

class Question(db.Model):
    q_id = db.Column(db.Integer, primary_key=True)
    chapter_name = db.Column(db.String(), nullable=False)
    question = db.Column(db.String(), nullable=False)
    option_1 = db.Column(db.String(), nullable=False)
    option_2 = db.Column(db.String(), nullable=False)
    option_3 = db.Column(db.String(), nullable=False)
    option_4 = db.Column(db.String(), nullable=False)
    correct_option = db.Column(db.String(), nullable=False)
    question_mark = db.Column(db.Integer, nullable=False)
    hint = db.Column(db.String())

    def __init__(self, chapter_name, question, option_1, option_2, option_3, option_4, correct_option, question_mark, hint=""):
        self.chapter_name = chapter_name
        self.question = question
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.correct_option = correct_option
        self.question_mark = question_mark
        self.hint = hint

    def __repr__(self):
        return f"{self.q_id}:{self.chapter_name}:{self.question[:len(self.question) // 2]}"
