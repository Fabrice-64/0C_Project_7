from nltk.internals import find_jars_within_path
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from tests.conftest import Path

# Alternatively to setting the CLASSPATH add the jar and model via their path:
original_question = 'Bonjour ChatBot, pourrais-tu me parler des Champs-Elysées,\
    à Paris ? Bisous à tout le monde'
expected_answer = 'Champs-Elysées'




def func_pos_tagger(model, jar, original_question):
    pos_tagger = StanfordPOSTagger(model, jar)
    # Add other jars from Stanford directory
    stanford_dir = pos_tagger._stanford_jar.rpartition('/')[0]
    stanford_jars = find_jars_within_path(stanford_dir)
    pos_tagger._stanford_jar = ':'.join(stanford_jars)
    res = pos_tagger.tag(word_tokenize(original_question))
    return res


def test_question_parser():
    assert func_pos_tagger(Path.PATH_TO_MODEL, Path.PATH_TO_JAR, original_question) == expected_answer
