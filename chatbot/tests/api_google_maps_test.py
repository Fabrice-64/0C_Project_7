import requests
from nose.tools import assert_true

from config import Config

GOOGLE_ROOT = 'https://maps.googleapis.com/maps/api/staticmap'

GOOGLE_PAYLOAD = {
    'center': 'Hôtel des Invalides',
    'size': '400x400',
    'key': Config.GOOGLE_API_KEY,
    'zoom': '13',
    'scale': '2',
    'format': 'jpg',
    'language': 'fr',
    'markers': 'size:mid|color:red|Hôtel des Invalides'
}

def test_connection_ok():
    response = requests.get(GOOGLE_ROOT, params=GOOGLE_PAYLOAD)
    assert_true(response.ok)

def test_get_map_ok():
    response = requests.get(GOOGLE_ROOT, params=GOOGLE_PAYLOAD)
    response_type = response.headers['Content-Type']
    assert response_type == 'image/jpeg'
    assert response.content != None