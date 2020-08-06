from config import Config

# Use with nltk to call the stanford project language analysis


class Path():
    ROOT = '/Users/fabricejaouen/DepotLocalGIT/OC_Project_7'
    JAR = '/chatbot/resources/stanford-tagger-4.0.0/stanford-postagger.jar'
    MODEL = '/chatbot/resources/stanford-tagger-4.0.0/models/french-ud.tagger'

    PATH_TO_JAR = ROOT + JAR
    PATH_TO_MODEL = ROOT+MODEL


class WikipediaPath():

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


class GooglePath():
    GOOGLE_ROOT = 'https://maps.googleapis.com/maps/api/staticmap'
    GOOGLE_PAYLOAD = {
            'center': 'TBD',
            'size': '400x400',
            'key': Config.GOOGLE_API_KEY,
            'zoom': '13',
            'scale': '2',
            'format': 'jpg',
            'language': 'fr',
            'markers': 'size:mid|color:red|'}