"""
    This module tests the parser, as revealed by its name.
    The first tests are unitary tests, the last one is functional
    as it test all the methods leading to a parsed sentence.

    Exceptions:
    NIL

    Functions.
    NIL
    """
from config import StanfordPath
import pytest
from pytest import mark
from tests.conftest import TestParameters
from app.controller.question_parser import QuestionParser

# Are needed to test the tagging process.
path = StanfordPath()
jar, model = path.get_path_stanford_tagger()


class TestQuestion(QuestionParser):

    @mark.parametrize("test_input, expected",
                      TestParameters.questions_tokenize)
    def test_remove_stop_words(self, test_input, expected):
        result = self._remove_stop_words(test_input)
        assert result == expected

    @mark.parametrize("test_input, expected", TestParameters.tag_tokens)
    def test_tag_words(self, test_input, expected):
        assert self._tag_words(jar, model, test_input) == expected

    @mark.parametrize("test_input, expected", TestParameters.filtered_words)
    def test_discard_words(self, test_input, expected):
        assert self._discard_words(test_input) == expected

    @mark.parametrize("test_input, expected", TestParameters.parsing_process)
    def test_full_parsing_process(self, test_input, expected):
        result = self.parsing_process(test_input)
        assert result == expected
