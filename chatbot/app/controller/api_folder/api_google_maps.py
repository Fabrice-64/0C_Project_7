import requests
from app.controller.config import GooglePath as GP


class GoogleApi:

    def _response_google(self, exact_location):
        GP.GOOGLE_PAYLOAD['center'] = exact_location
        markers = 'size:mid|color:red|' + exact_location
        GP.GOOGLE_PAYLOAD['markers'] = markers
        response = requests.get(GP.GOOGLE_ROOT, params=GP.GOOGLE_PAYLOAD)
        return response

    def get_map(self, exact_location):
        response = self._response_google(exact_location)
        return response.url
