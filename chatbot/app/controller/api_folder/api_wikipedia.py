import requests
import re

from app.controller import config


def get_draft_location(location_search):
    WIKI_DRAFT_LOCATION_PAYLOAD = {
                                    'format': 'json',
                                    'action': 'query',
                                    'list': 'search',
                                    'srsearch': 'TBD',
                                    'srlimit': '1'}
    payload = WIKI_DRAFT_LOCATION_PAYLOAD
    payload['srsearch'] = location_search
    response = requests.get(config.WIKI_ROOT, params=payload)
    if response.ok:
        return response
    else:
        return None


def sort_out_exact_location_name(draft_location):
    exact_location_name = draft_location['query']['search'][0]['title']
    return exact_location_name


def get_location_summary(exact_location_name):
    WIKI_GET_LOCATION_SUMMARY_PAYLOAD = {
                                                'format': 'json',
                                                'action': 'query',
                                                'titles': 'TBD',
                                                'propr': 'extract',
                                                'exintro': '1'}
    payload = WIKI_GET_LOCATION_SUMMARY_PAYLOAD
    payload['titles'] = exact_location_name
    response = requests.get(config.WIKI_ROOT, params = payload)
    if response.ok:
        return response
    else:
        return None


def extract_location_summary(draft_location_summary):
    key = list(draft_location_summary.get('query').get('pages').keys())
    response = draft_location_summary.get('query').get('pages').get(key[0]).get('extract')
    return response


def filter_location_summary(non_filtered_location_summary):
    filtered_location_summary = re.sub('<.*?>', "", non_filtered_location_summary)
    return filtered_location_summary


def get_coordinates(exact_location_name):
    WIKI_GET_COORDINATES_PAYLOAD = {
                                    'format': 'json',
                                    'action': 'query',
                                    'titles': 'TBD',
                                    'prop': 'coordinates'}
    payload = WIKI_GET_COORDINATES_PAYLOAD
    payload['titles'] = exact_location_name
    response = requests.get(config.WIKI_ROOT, params = payload)
    return response


def filter_coordinates(draft_coordinates):
    key = list(draft_coordinates.get('query').get('pages').keys())
    filtered_coordinates = draft_coordinates.get('query').get('pages').get(key[0]).get('coordinates')[0]
    
    return filtered_coordinates
