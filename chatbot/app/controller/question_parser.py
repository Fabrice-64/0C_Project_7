
import re
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize, wordpunct_tokenize
from resources import stop_words
from app.controller.config import Path

jar = Path.PATH_TO_JAR
model = Path.PATH_TO_MODEL


class QuestionParser():

    def remove_stop_words(self, original_question):
        tokens = wordpunct_tokenize(original_question)
        cleaned_sentence =\
            [w for w in tokens if w not in stop_words.stop_words_french]
        return " ".join(cleaned_sentence)

    def tag_words(self, jar, model, cleaned_sentence):
        pos_tagger = StanfordPOSTagger(model, jar, encoding="utf-8")
        tagged_words = pos_tagger.tag(word_tokenize(cleaned_sentence))
        return tagged_words

    def discard_words(self, tagged_words):
        key_words = []
        for i in range(len(tagged_words)):
            if 'VERB' == tagged_words[i][1]:
                while i < len(tagged_words) - 1 \
                    and tagged_words[i+1][1] in ['NOUN', 'PROPN'] \
                    and re.match("[A-Z]+[a-z]{1,18}", tagged_words[i+1][0]):
                    key_words.append(tagged_words[i+1][0])
                    i += 1
        key_words = " ".join(key_words)
        return key_words

    def parsing_process(self, original_question):
        self.cleaned_sentence = self.remove_stop_words(original_question)
        self.tagged_words = self.tag_words(jar, model, self.cleaned_sentence)
        self.key_words = self.discard_words(self.tagged_words)
        return self.key_words
