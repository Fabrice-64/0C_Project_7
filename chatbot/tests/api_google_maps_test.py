import requests
from nose.tools import assert_true
from app.controller.api_folder.api_google_maps import get_map

from config import Config

test_location = "Hôtel des Invalides"


def test_connection_ok():
    response = get_map("Hôtel des Invalides")
    assert_true(response.ok)


def test_get_map_ok():
    response = get_map("Hôtel des Invalides")
    response_type = response.headers['Content-Type']
    assert response_type == 'image/jpeg'
    assert response.content != None
