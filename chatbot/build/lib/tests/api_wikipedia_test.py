import requests
from app.controller import config

from pytest import mark
from tests.conftest import TestConfigureKeyWords


def configure_keywords(keywords):
    keywords = "%20".join(keywords.split())
    return keywords


def set_request(keywords):
    return set_request.format(keywords)


@mark.parametrize("test_input, expected", TestConfigureKeyWords.strings_to_test)
def test_configure_keywords(test_input, expected):
    assert configure_keywords(test_input) == expected


def test_connection_ok():
    r = requests.get(config.WIKI_ROOT)
    assert r.status_code == 200