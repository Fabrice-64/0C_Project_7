"""
   This module parses the question in successive steps.
   
    Classes:
    QuestionParser: regroups all the methods involved in the parsing process.

    Exceptions:
    NIL

    Functions:
    NIL
    """

from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize, wordpunct_tokenize
from resources import stop_words
from app.controller.config import Path

# this two constants are needed to use the StanfordPOSTagger functionality
jar = Path.PATH_TO_JAR
model = Path.PATH_TO_MODEL


class QuestionParser:

    def _remove_stop_words(self, original_question):
        tokens = wordpunct_tokenize(original_question)
        cleaned_sentence =\
            [w for w in tokens if w not in stop_words.stop_words_french]
        return " ".join(cleaned_sentence)

    def _tag_words(self, jar, model, cleaned_sentence):
        pos_tagger = StanfordPOSTagger(model, jar, encoding="utf-8")
        tagged_words = pos_tagger.tag(word_tokenize(cleaned_sentence))
        return tagged_words

    def _discard_words(self, tagged_words):
        key_words = []
        question_tag = ('?', 'PUNCT')
        if question_tag in tagged_words:
            index = tagged_words.index(question_tag)
            while index > 0 and tagged_words[index-1][1] not in \
                    ['PUNCT', 'VERB', 'INTJ', 'ADV', 'DET', 'ADP', 'PRON']:
                key_words.append(tagged_words[index-1][0])
                index -= 1
            key_words = " ".join(list(reversed(key_words)))
        else:
            key_words = 'None'
        return key_words

    def parsing_process(self, original_question):
        cleaned_sentence = self._remove_stop_words(original_question)
        tagged_words = self._tag_words(jar, model, cleaned_sentence)
        key_words = self._discard_words(tagged_words)
        return key_words
