from flask import render_template, flash, request
from app import app
from app.forms import QuestionForm


@app.route('/')
@app.route('/interface', methods=['GET', 'POST'])
def interface():
    question = QuestionForm()
    return render_template('interface.html', title='Home', question=question)
