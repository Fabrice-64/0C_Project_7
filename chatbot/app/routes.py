from flask import render_template, flash, request
from app import app
from app.forms import QuestionForm
from app.controller import question_parser

@app.route('/')
@app.route('/interface', methods=['GET', 'POST'])
def interface():
    question = QuestionForm()
    if request.method == 'POST' and question.validate():
        flash('La question est: {}'.format(question.question.data))
        question_parser.question_to_parse.append(question.question.data)
        print('Response: {}'.format(question_parser.question_to_parse[0]))
    return render_template('interface.html', title='Home', question=question)
