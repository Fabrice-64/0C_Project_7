import re
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize, wordpunct_tokenize
from app.controller.config import Path

import pytest
from pytest import mark
from tests.conftest import TestParameters
from app.controller.question_parser import QuestionParser

jar = Path.PATH_TO_JAR
model = Path.PATH_TO_MODEL


class TestQuestion():


    @mark.parametrize("test_input, expected", TestParameters.questions_tokenize)
    def test_remove_stop_words(self, test_input, expected):
        assert QuestionParser.remove_stop_words(self, test_input) == expected


    @mark.parametrize("test_input, expected", TestParameters.tag_tokens)
    def test_tag_words(self, test_input, expected):
        assert QuestionParser.tag_words(self, jar, model, test_input) == expected


    @mark.parametrize("test_input, expected", TestParameters.filtered_words)
    def test_discard_words(self, test_input, expected):
        assert QuestionParser.discard_words(self, test_input) == expected


    @mark.parametrize("test_input, expected", TestParameters.parsing_process)
    def test_full_parsing_process(self, test_input, expected):
        test = QuestionParser()
        result = test.parsing_process(test_input)
        assert result == expected

