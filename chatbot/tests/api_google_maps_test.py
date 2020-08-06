import requests
from nose.tools import assert_true
from app.controller.api_folder.api_google_maps import GoogleApi

from config import Config

test_location = "Hôtel des Invalides"


class TestGoogleApi(GoogleApi):
    def test_connection_ok(self):
        response = self.get_map(test_location)
        assert_true(response.ok)

    def test_get_map_ok(self):
        response = self.get_map(test_location)
        response_type = response.headers['Content-Type']
        assert response_type == 'image/jpeg'
