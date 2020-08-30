from flask import render_template, request, jsonify
from app import app
from app.controller.question_processing import QuestionProcessing


@app.route('/')
def question():
    return render_template('question.html')


@app.route('/process_question')
def process_question():
    question = request.args.get('question', "None", type=str)
    processed_question = QuestionProcessing()
    processed_question = processed_question.question_processing(question)
    return jsonify(question=processed_question[0],
                   wikipedia_response=processed_question[1],
                   google_map=processed_question[2])
