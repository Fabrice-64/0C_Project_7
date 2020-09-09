"""
   This module checks the connection to Google maps.

    Classes:
    TestGoogleApi

    Exceptions:
    NIL

    Functions:
    NIL
    """

import pytest
from pytest import mark
from app.controller.api_folder.api_google_maps import GoogleApi
from tests.conftest import TestGoogleApiParams as TGAP


class TestGoogleApi(TGAP,GoogleApi):
    """
        Basic development. As for now only the connection is tested (code 200)
        """
    @mark.parametrize("test_input, expected", TGAP.test_google_params)
    def test_connection_dynamic_ok(self, test_input, expected):
        response = self.get_map_dynamic(test_input)
        assert response == expected
