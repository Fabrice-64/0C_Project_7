"""
   This module checks the connectin with Google Maps API

    Classes:
    TestGoogleApi: regroups all the methods involved in the API.

    Exceptions:
    NIL

    Functions:
    NIL
    """
from app.controller.api_folder.api_google_maps import GoogleApi
from tests.conftest import TestGoogleApiParams as TGAP
from pytest import mark


class TestGoogleApi(GoogleApi, TGAP):

    @mark.parametrize("test_input, expected",
                      TGAP.test_google_params)
    def test_connection_ok(self, test_input, expected):
        response = self.get_map_dynamic(test_input)
        assert response == expected
