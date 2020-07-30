import requests

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
    return response
