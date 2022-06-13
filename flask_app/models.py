from flask_app import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String, nullable=False)
    correct_answer = db.Column(db.String, nullable=False)
    answers = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return f'Question: {self.question_text}, correct answer: {self.correct_answer}, options: {self.answers}'

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_finished = db.Column(db.DateTime, nullable=True)
    answers = db.Column(db.PickleType, nullable=False)
    score = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Score: {self.score}, at {self.time_finished} by {self.name}'
