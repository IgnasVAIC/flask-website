from flask_app import app
from flask import render_template, url_for, flash, redirect, request
from flask_app import models, db
from random import shuffle
from datetime import datetime

questions = models.Question.query.all()


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':

            time_finished = datetime.utcnow()
            picked_options = []
            correct = 0
            for question in questions:
                form_name = str(question.id)
                answer = request.form[form_name]
                if answer == question.correct_answer:
                    correct += 1
                picked_options.append(answer)
            name = request.form["name"]
            score = correct / (len(questions))
            result1 = models.Result(time_finished = time_finished, answers = picked_options, score=score, name=name)
            db.session.add(result1)
            db.session.commit()
            return render_template('result.html', score=score, questions=questions, picked_options=picked_options)
    else:
        for question in questions:
            shuffle(question.answers)
        return render_template('quiz.html', questions=questions)

@app.route("/result", methods=['GET', 'POST'])
def result():
        return render_template('result.html')

@app.route("/scores")
def scores():
    results = models.Result.query.all()
    results.sort(key=lambda x: x.score, reverse=True)
    return render_template('scores.html', results=results)