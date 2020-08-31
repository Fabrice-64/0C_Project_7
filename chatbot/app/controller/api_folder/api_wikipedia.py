"""
   This module progressively extracts the data from wikipedia web-site

    Classes:
    WikipediaApi

    Exceptions:
    NIL

    Functions:
    NIL
    """

import requests
import re
from app.controller.config import WikipediaPath as WP


class WikipediaApi():
    """
        Gets the summary of a Wikipedia article. Sends first the rough name extracted from the question parsing, then 
        gets the exact name of the article and downloads the summary.
        Methods extracting the coordinates available in the article are extracted but not used.

        Methods:

        _get_draft_location:
        sends to WIkipedia the rough data

        _sort_out_exact_location_name:
        exploit the response to find the exact name of the article. In case of several responses, take the first one.

        _push_exact_location_name:
        sends it to the route to be used by Google.

        _get_location_summary:
        fetches the summary from Wikipedia website.

        _extract_location_summary:
        from wikipedia response gets the string with the summary.

        _filter_location_summary:
        removes the html caracters from the summary.

        _get_coordinates:
        not used in the current version.

        _extract_coordinates:
        not used in the current version.

        from_location_to_summary:
        gathers all steps from getting a location summary to its sending
        to the routes module.
        """

    def _get_draft_location(self, location_search):
        """
            Arguments:
            location_search: outcome of question parsing.
        
            Returns:
            API response on JSON format.
            """
        payload = WP.WIKI_DRAFT_LOCATION_PAYLOAD
        payload['srsearch'] = location_search
        response = requests.get(WP.WIKI_ROOT, params=payload)
        if response.ok:
            return response.json()
        else:
            return None

    def _sort_out_exact_location_name(self, draft_location):
        """
            Arguments:
            draft_location

            Returns:
            exact_location_name: exact name of the location.
            Corresponds to a wikipedia article.
            """
        try:
            exact_location_name = draft_location['query']['search'][0]['title']
            return exact_location_name
        except:
            return "None"

    def push_exact_location_name(self, location_search):
        """
            Arguments:
            location_search

            Returns:
            exact_location_name: exact name of the location.
            Corresponds to a wikipedia article.
            """
        location = self._get_draft_location(location_search)
        exact_location_name = self._sort_out_exact_location_name(location)
        return exact_location_name

    def _get_location_summary(self, full_location_name):
        """
            Arguments:
            full_location_name: string with the title of the wikipedia article

            Returns:
            response: location summary in JSON format. Corresponds to a wikipedia article.
            """
        payload = WP.WIKI_GET_LOCATION_SUMMARY_PAYLOAD
        payload['titles'] = full_location_name
        response = requests.get(WP.WIKI_ROOT, params=payload)
        if response.ok:
            return response.json()
        else:
            return "None"

    def _extract_location_summary(self, draft_location_summary):
        """
            Arguments:
            draft_location_summary: summary is embeded in a JSON file

            Returns:
            response: string extracted from the JSON file.
            """
        key = list(draft_location_summary.get('query').get('pages').keys())
        response = draft_location_summary.get('query').get(
            'pages').get(key[0]).get('extract')
        return response

    def _filter_location_summary(self,
                                 non_filtered_location_summary):
        """
            Arguments:
            non_filtered_location_summary: contains HTML characters

            Returns:
            filtered_location_summary: string without the HTML tags.
            """
        filtered_location_summary = re.sub(
            '<.*?>', "", non_filtered_location_summary)
        return filtered_location_summary

    def _get_coordinates(self, exact_location_name):
        """
            Arguments:
            exact_location_name: needed by wikipedia to find the article and then the coordinates

            Returns:
            response: coordinates embedded in JSON format
            """
        payload = WP.WIKI_GET_COORDINATES_PAYLOAD
        payload['titles'] = exact_location_name
        response = requests.get(WP.WIKI_ROOT, params=payload)
        response = response.json()
        return response

    def _filter_coordinates(self, draft_coordinates):
        """
            Arguments:
            draft_coordinates: are in JSON format

            Returns:
            filtered_coordinates: tuple containing the long and lat.
            """
        try:
            key = list(draft_coordinates.get('query').get('pages').keys())
            filtered_coordinates = draft_coordinates.get('query').get(
                'pages').get(key[0]).get('coordinates')[0]
            return filtered_coordinates
        except TypeError:
            return "None"

    def from_location_to_summary(self, location):
        """
            Unfold the complete process from the location input to a clean summary.
            Arguments:
            location

            Returns:
            response: location summary.
            """
        if location != "None":
            response = self._get_location_summary(location)
            response = self._extract_location_summary(response)
            response = self._filter_location_summary(response)
            return response
        else:
            return "None"
