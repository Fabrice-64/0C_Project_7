"""
    This module manages the relation between the client and the server.

    Classes:
    NIL

    Exceptions:
    NIL

    Functions:
    question: 
    just needed to display the default page.

    process_question: 
    gets the question from the client, 
    sends it, gets the result back and sends it to the front.
    """
from flask import render_template, request, jsonify
from app import app
from app.controller.question_processing import QuestionProcessing


@app.route('/')
def question():
    """
        Its role is to display the main page.
        """
    return render_template('question.html')


@app.route('/process_question', methods=['GET', 'POST'])
def process_question():
    """
        Manages the whole process from the client to the server and back.
        """
    question = request.args.get('question', "None", type=str)
    processed_question = QuestionProcessing()
    processed_question = processed_question.question_processing(question)
    return jsonify(wikipedia_response=processed_question[0],
                   url_google_dynamic=processed_question[1])
