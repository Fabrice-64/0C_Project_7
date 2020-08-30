from app.controller.question_parser import QuestionParser
from app.controller.api_folder.api_wikipedia import WikipediaApi
from app.controller.api_folder.api_google_maps import GoogleApi


class QuestionProcessing:

    def question_processing(self, question):
        question_to_parse = QuestionParser()
        parsed_question = WikipediaApi()
        google_map = GoogleApi()
        request_to_send = question_to_parse.parsing_process(question)
        exact_location =\
            parsed_question.push_exact_location_name(request_to_send)
        wikipedia_response = parsed_question.from_location_to_summary(
            exact_location)
        google_map = google_map.get_map(exact_location)
        return (question, wikipedia_response, google_map)
