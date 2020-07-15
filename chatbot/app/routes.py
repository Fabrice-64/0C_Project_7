from flask import render_template
from app import app
from app.forms import Question


@app.route('/')
@app.route('/interface')
def interface():
    question = Question()
    return render_template('interface.html', title='Home', question=question)
