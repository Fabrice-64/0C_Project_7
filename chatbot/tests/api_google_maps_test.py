import requests
import pytest
from app.controller.api_folder.api_google_maps import GoogleApi

test_location = "Hôtel des Invalides"


class TestGoogleApi(GoogleApi):

    def test_connection_ok(self):
        response = self.response_google("Hotel des Invalides")
        assert response.status_code == 200


