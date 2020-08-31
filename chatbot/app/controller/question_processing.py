"""
   This module parses the question in successive steps.

    Classes:
    QuestionParser: regroups all the methods involved in the parsing process.

    Exceptions:
    NIL

    Functions:
    NIL
    """
from app.controller.question_parser import QuestionParser
from app.controller.api_folder.api_wikipedia import WikipediaApi
from app.controller.api_folder.api_google_maps import GoogleApi


class QuestionProcessing:
    """
        Operate the whole process from the parsing of a question
        down to sending the response to the client.

        Methods:
        question_processing:
        manages the whole process fetched from the route and sent back.
        """

    def question_processing(self, question):
        """
            Arguments:
            question: as asked by the user.

            Returns:
            (question, wikipedia_response, google_map):
            a tuple containing all the items needed to operate
            the chatbot.
            """
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
