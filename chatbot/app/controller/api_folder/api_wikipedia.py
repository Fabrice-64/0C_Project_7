import requests
import re
from app.controller.config import WikipediaPath as WP


class WikipediaApi():
    def get_draft_location(self, location_search):
        payload = WP.WIKI_DRAFT_LOCATION_PAYLOAD
        payload['srsearch'] = location_search
        response = requests.get(WP.WIKI_ROOT, params=payload)
        if response.ok:
            return response.json()
        else:
            return None

    def sort_out_exact_location_name(self, draft_location):
        try:
            exact_location_name = draft_location['query']['search'][0]['title']
            return exact_location_name
        except:
            return "None"
    
    def push_exact_location_name(self, location_search):
        location = self.get_draft_location(location_search)
        exact_location_name = self.sort_out_exact_location_name(location)
        return exact_location_name

    def get_location_summary(self, full_location_summary):
        payload = WP.WIKI_GET_LOCATION_SUMMARY_PAYLOAD
        payload['titles'] = full_location_summary
        response = requests.get(WP.WIKI_ROOT, params=payload)
        if response.ok:
            return response.json()
        else:
            return "None"

    def extract_location_summary(self, draft_location_summary):
        key = list(draft_location_summary.get('query').get('pages').keys())
        response = draft_location_summary.get('query').get('pages').get(key[0]).get('extract')
        return response

    def filter_location_summary(self, non_filtered_location_summary):
        filtered_location_summary = re.sub('<.*?>', "", non_filtered_location_summary)
        return filtered_location_summary

    def get_coordinates(self, exact_location_name):
        payload = WP.WIKI_GET_COORDINATES_PAYLOAD
        payload['titles'] = exact_location_name
        response = requests.get(WP.WIKI_ROOT, params=payload)
        response = response.json()
        return response

    def filter_coordinates(self, draft_coordinates):
        try:
            key = list(draft_coordinates.get('query').get('pages').keys())
            filtered_coordinates = draft_coordinates.get('query').get('pages').get(key[0]).get('coordinates')[0]
            return filtered_coordinates
        except TypeError:
            return "None"

    def from_location_to_summary(self, location):
        if location != "None":
            response = self.get_location_summary(location)
            response = self.extract_location_summary(response)
            response = self.filter_location_summary(response)
            return response
        else:
            return "None"
