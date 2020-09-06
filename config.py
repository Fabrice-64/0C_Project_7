"""
   This module manages all the parameters needed for the APIS

    Classes:
    Path: used for the tokenization of the question string.
    Needed for the parsing

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


class NLTKData:
    def __init__(self):
        self.NLTK_DATA = 'resources/nltk_data'
        reg = re.compile(r'^(.*?(/tests))')
        current_dir = os.getcwd()
        if reg.match(current_dir):
            self.ROOT = os.path.dirname(os.getcwd())
        else:
            self.ROOT = os.getcwd()
"""
    def get_path_nltk_data(self):
        PATH_TO_NLTK_DATA = os.path.join(self.ROOT, self.NLTK_DATA)
        return PATH_TO_NLTK_DATA
"""

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
    GOOGLE_ROOT = 'https://maps.googleapis.com/maps/api/staticmap'
    GOOGLE_PAYLOAD = {
        # Center the map on the name of the wikipedia article
        'center': 'TBD',
        # Size is in pixels
        'size': '600x600',
        # Confidential key for the API: stored apart
        'key': Config.GOOGLE_API_KEY,
        # For the zoom: the higher the figure is, the smaller the scale is.
        'zoom': '12',
        'scale': '2',
        'format': 'jpg',
        'language': 'fr',
        # Highlights the location at the center of the map.
        'markers': 'size:mid|color:red|'}

"""
nltk = NLTKData()
nltk_data = nltk.get_path_nltk_data()


os.environ['NLTK_DATA'] = nltk_data
"""