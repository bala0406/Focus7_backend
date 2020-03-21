from flask import jsonify
from random import randint


from Models.models import Question
from app import app
from app import db


@app.route("/getquestions", methods=["GET"])
def getQuestions():

    questionsList = []
    rowCount = Question.query.all().count()
    # questionDict = {}
    for i in range(7):
        
        question = Question.query.get(randint(1, rowCount))
        chapter_name = question.chapter_name
        quest_ion = question.question
        option_1 = question.option_1
        option_2 = question.option_2
        option_3 = question.option_3
        option_4 = question.option_4
        correct_option = question.correct_option
        question_mark = question.question_mark
        hint = question.hint if question.hint is not None else ""
        questionDict = {
            "chapter_name": chapter_name,
            "question": quest_ion,
            "option_1": option_1,
            "option_2": option_2,
            "option_3": option_3,
            "option_4": option_4,
            "correct_option": correct_option,
            "question_mark": question_mark,
            "hint": hint
        }
        questionsList.append(questionDict)
    return jsonify(questionsList)
