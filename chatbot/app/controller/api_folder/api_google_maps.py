"""
   This module gets a static map from Google.
   
    Classes:
    GoogleApi

    Exceptions:
    NIL

    Functions:
    NIL
    """
import requests
from app.controller.config import GooglePath as GP


class GoogleApi:
    """
        Check the class GooglePath in module controller.config.
        To be noticed: the API key is in a separate module. The user should
        get his own confidential key.

        Methods:

        _response_google:
        gathers all data needed for the API.
        Used for testing purposes as well.

        get_map:
        extracts the url from the response to the API request.
        """

    def _response_google(self, exact_location):
        GP.GOOGLE_PAYLOAD['center'] = exact_location
        markers = 'size:mid|color:red|' + exact_location
        GP.GOOGLE_PAYLOAD['markers'] = markers
        response = requests.get(GP.GOOGLE_ROOT, params=GP.GOOGLE_PAYLOAD)
        return response

    def get_map(self, exact_location):
        """
            Public method as used in other modules.
            """
        response = self._response_google(exact_location)
        return response.url
