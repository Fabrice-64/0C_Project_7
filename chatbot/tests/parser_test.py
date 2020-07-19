from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from pytest import mark
from tests.conftest import Path, TestParameters


def tag_words(model, jar, original_question):
    pos_tagger = StanfordPOSTagger(model, jar, encoding="utf-8")
    tagged_words = pos_tagger.tag(word_tokenize(original_question))
    return tagged_words


@mark.parametrize("test_input, expected", TestParameters.questions)
def test_question_parser(test_input, expected):
    assert tag_words(Path.PATH_TO_MODEL, Path.PATH_TO_JAR, test_input
                     ) == expected
