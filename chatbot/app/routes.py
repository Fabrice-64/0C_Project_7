from flask import render_template, flash, request
from app import app
from app.forms import QuestionForm
from app.controller.question_parser import QuestionParser
from app.controller.api_folder.api_wikipedia import WikipediaApi

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
        parsed_question = WikipediaApi()
        wikipedia_response = parsed_question.from_question_to_summary(request_to_send)
        print(wikipedia_response)
    return render_template('interface.html', title='Home', question=question)
