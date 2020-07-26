import requests
from app.controller import config

from pytest import mark
from tests.conftest import TestConfigureKeyWords


def configure_keywords(keywords):
    keywords = "%20".join(keywords.split())
    return keywords


def set_request(keywords):
    return config.WIKI_ROOT.format(keywords)


def get_summary():
    pass


@mark.parametrize("test_input, expected", TestConfigureKeyWords.strings_to_test)
def test_configure_keywords(test_input, expected):
    assert configure_keywords(test_input) == expected


@mark.parametrize("test_input, expected", TestConfigureKeyWords.strings_to_test)
def test_connection_ok(test_input, expected):
    keywords = configure_keywords(test_input)
    get_summary = set_request(keywords)
    r = requests.get(get_summary)
    assert keywords == expected
    assert r.status_code == 200