import requests
from app.controller.config import GooglePath as GP


class GoogleApi:

    def get_map(self, exact_location):
        GP.GOOGLE_PAYLOAD['center'] = exact_location
        markers = 'size:mid|color:red|' + exact_location
        GP.GOOGLE_PAYLOAD['markers'] = markers
        response = requests.get(GP.GOOGLE_ROOT, params=GP.GOOGLE_PAYLOAD)
        return response.url
