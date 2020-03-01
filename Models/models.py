from app import db

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


    def __repr__(self):
        return f"{self.id}:{self.chapter_name}:{self.question[:len(self.question) // 2]}"
