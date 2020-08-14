from flask import render_template, flash, request
from app import app
from app.forms import QuestionForm
from app.controller.question_parser import QuestionParser
from app.controller.api_folder.api_wikipedia import WikipediaApi
from app.controller.api_folder.api_google_maps import GoogleApi


@app.route('/')
@app.route('/question', methods=['GET', 'POST'])
def question():
    question = QuestionForm()
    wikipedia_response=""
    google_map = ""
    if question.validate_on_submit():
        question_to_parse = QuestionParser()
        request_to_send = question_to_parse.parsing_process(question.question.data)
        parsed_question = WikipediaApi()
        exact_location = parsed_question.push_exact_location_name(request_to_send)
        wikipedia_response = parsed_question.from_location_to_summary(exact_location)
        google_map = GoogleApi()
        google_map = google_map.get_map(exact_location)

    return render_template('question.html', question=question, wikipedia_response=wikipedia_response, google_map=google_map)
