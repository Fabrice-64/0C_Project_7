from flask import render_template, flash, request
from app import app
from app.forms import QuestionForm
from app.controller.question_parser import QuestionParser

@app.route('/')
@app.route('/interface', methods=['GET', 'POST'])
def interface():
    question = QuestionForm()
    if request.method == 'POST' and question.validate():
        flash('La question est: {}'.format(question.question.data))
        question_to_parse = QuestionParser()
        print(question.question.data)
        request_to_send = question_to_parse.parsing_process(question.question.data)
        print(request_to_send)
    return render_template('interface.html', title='Home', question=question)
