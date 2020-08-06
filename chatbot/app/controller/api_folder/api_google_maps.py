import requests
from config import Config

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


def get_map(exact_location):
    GOOGLE_PAYLOAD['center'] = exact_location
    markers = 'size:mid|color:red' + exact_location
    GOOGLE_PAYLOAD['markers'] = markers
    response = requests.get(GOOGLE_ROOT, params=GOOGLE_PAYLOAD)
    return response
