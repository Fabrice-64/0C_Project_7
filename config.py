"""
   This module manages all the parameters needed for the APIS

    Classes:

    Config: contains some environment variables, mainly used for local.

    StanfordPath: StanfordPOSTagger performs the syntaxtic analysis of the question.
    The path to the files performing this task is defined here.

    WikipediaPath: needed for the API

    GooglePath: needed for the API.
    To be noticed: this is were the parameters
    of the downloaded map can be changed.

    Exceptions:
    NIL

    Functions:
    NIL
    """

import os
import re
from dotenv import load_dotenv

load_dotenv()


class Config(object):

    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    FLASK_APP = os.environ.get("chatbot.py")
    ROOT = os.getcwd()


class StanfordPath:
    def __init__(self):
        self.JAR = 'resources/stanford-tagger-4.0.0/stanford-postagger.jar'
        self.MODEL = 'resources/stanford-tagger-4.0.0/models/french-ud.tagger'
        reg = re.compile(r'^(.*?(/tests))')
        current_dir = os.getcwd()
        if reg.match(current_dir):
            self.ROOT = os.path.dirname(os.getcwd())
        else:
            self.ROOT = os.getcwd()

    def get_path_stanford_tagger(self):
        PATH_TO_JAR = os.path.join(self.ROOT, self.JAR)
        PATH_TO_MODEL = os.path.join(self.ROOT, self.MODEL)
        return PATH_TO_JAR, PATH_TO_MODEL


class WikipediaPath:
    # The values with TBD mean that they are filled during the API process
    WIKI_ROOT = 'https://fr.wikipedia.org/w/api.php'
    WIKI_DRAFT_LOCATION_PAYLOAD = {
        'format': 'json',
        'action': 'query',
        'list': 'search',
        'srsearch': 'TBD',
        'srlimit': '1'}
    WIKI_GET_LOCATION_SUMMARY_PAYLOAD = {
        'format': 'json',
        'action': 'query',
        'titles': 'TBD',
        'prop': 'extracts',
        'exintro': '1'}
    WIKI_GET_COORDINATES_PAYLOAD = {
        'format': 'json',
        'action': 'query',
        'titles': 'TBD',
        'prop': 'coordinates'}


class GooglePath:

    GOOGLE_ROOT_DYNAMIC = 'https://www.google.com/maps/embed/v1/place?'
    GOOGLE_PAYLOAD_DYNAMIC = {
        'key': Config.GOOGLE_API_KEY,
        'q': 'TBD',
        'language': 'fr',
        'zoom': '11',
        'region': 'fr'
    }
