"""
   This module parses the question in successive steps.

    Classes:
    QuestionParser: regroups all the methods involved in the parsing process.

    Exceptions:
    NIL

    Functions:
    NIL
    """

from resources import stop_words
from config import StanfordPath
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize, wordpunct_tokenize

# this two constants are needed to use the StanfordPOSTagger functionality
path = StanfordPath()
jar, model = path.get_path_stanford_tagger()


class QuestionParser:
    """
        Parsing is implemented step by step.
        At the bottom, all the methods are gathered into one single
        method in order to perform the whole process.

        Methods:
        _remove_stop_words:
        self explanatory

        _tag_words:
        assigns a syntaxic value to each word.

        _discard_words:
        discards some words iaw their syntaxic value.

        _parsing_process:
         operates the 3 previous methods.
        """

    def _remove_stop_words(self, original_question):
        """
            Arguments:
            original_question: comes from the client as such.

            Returns:
            a string withount the stop words (i.e. words which do not
            bring so much to the analyse of the question).
            """
        tokens = wordpunct_tokenize(original_question)
        cleaned_sentence =\
            [w for w in tokens if w not in stop_words.stop_words_french]
        return " ".join(cleaned_sentence)

    def _tag_words(self, jar, model, cleaned_sentence):
        """
            Arguments:
            cleaned_sentence

            Returns:
            tagged_words: a list containing tuples i.e (word, syntactic value).
            """
        pos_tagger = StanfordPOSTagger(model, jar, encoding="utf-8")
        tagged_words = pos_tagger.tag(word_tokenize(cleaned_sentence))
        return tagged_words

    def _discard_words(self, tagged_words):
        """
            Arguments:
            tagged_words:
            list of tuples containing a word and its syntactic value.

            Returns:
            key_words:
            a string with the remaining words necessary for a search.
            """
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
        """
            Arguments:
            original_question

            Returns:
             key_words:
            a string with the remaining words necessary for a search.
            """
        cleaned_sentence = self._remove_stop_words(original_question)
        tagged_words = self._tag_words(jar, model, cleaned_sentence)
        key_words = self._discard_words(tagged_words)
        return key_words
