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
from urllib.parse import urlencode
from config import GooglePath as GP


class GoogleApi:
    """
        Check the class GooglePath in module controller.config.
        To be noticed: the API key is in a separate module. The user should
        get his own confidential key.

        Methods:

        _response_google_static:
        gathers all data needed for the API (static map)
        Used for testing purposes as well.

        get_map_static:
        extracts the url from the response to the API request.

        _response_google_dynamic:
        gathers all data needed for the API (dynamic map)
        Used for testing purposes as well.

        get_map_dynamic:
        extracts the url from the response to the API request.
        """

    def _response_google_static(self, exact_location):
        GP.GOOGLE_PAYLOAD_STATIC['center'] = exact_location
        markers = 'size:mid|color:red|' + exact_location
        GP.GOOGLE_PAYLOAD_STATIC['markers'] = markers
        response = requests.get(GP.GOOGLE_ROOT_STATIC,
                                params=GP.GOOGLE_PAYLOAD_STATIC)
        return response

    def get_map_static(self, exact_location):
        """
            Public method as used in other modules.
            """
        response = self._response_google_static(exact_location)
        return response.url

    def _create_url_google_dynamic(self):
        """
            At Google, the root for embedded maps is different from static maps.
            """
        GP.GOOGLE_PAYLOAD_DYNAMIC['q'] = GP.GOOGLE_PAYLOAD_STATIC['center']
        parameters = urlencode(GP.GOOGLE_PAYLOAD_DYNAMIC)
        url_google_dynamic = GP.GOOGLE_ROOT_DYNAMIC + parameters
        return url_google_dynamic

    def get_map_dynamic(self):
        """
            Public method as used in other modules.
            """
        url_google_dynamic = self._create_url_google_dynamic()
        return url_google_dynamic
