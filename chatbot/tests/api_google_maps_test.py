import pytest
from app.controller.api_folder.api_google_maps import GoogleApi
from tests.conftest import TestWikipediaRequest


class TestGoogleApi(GoogleApi, TestWikipediaRequest):

    def test_connection_ok(self):
        response = self._response_google(self.mock_location_name)
        assert response.status_code == 200
