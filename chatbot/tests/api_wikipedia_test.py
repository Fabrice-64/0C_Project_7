import requests
from app.controller import config
from app.controller.api_folder.api_wikipedia import WikipediaApi
from pytest import mark
from tests.conftest import TestWikipediaRequest
from nose.tools import assert_true, assert_equal
from unittest.mock import Mock, patch


class TestApiWikipedia(WikipediaApi):

    def test_connection_ok(self):
        response = requests.get(config.WIKI_ROOT)
        assert_true(response.ok)

    @patch('app.controller.api_folder.api_wikipedia.requests.get')
    def test_get_draft_location_when_response_is_ok(self, mock_get):
        mock_draft_location = TestWikipediaRequest.mock_draft_location
        location_search = TestWikipediaRequest.location_search
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_draft_location
        response = self.get_draft_location(location_search)
        assert_equal(response, mock_draft_location)

    def test_sort_out_exact_location_name(self):
        mock_location_name = TestWikipediaRequest.mock_location_name
        mock_draft_location = TestWikipediaRequest.mock_draft_location
        real_location_name = \
            self.sort_out_exact_location_name(mock_draft_location)
        assert_equal(mock_location_name, real_location_name)

    @patch('app.controller.api_folder.api_wikipedia.requests.get')
    def test_get_location_summary(self, mock_get):
        mock_location_name = TestWikipediaRequest.mock_location_name
        mock_location_summary = TestWikipediaRequest.mock_location_summary
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_location_summary
        response = self.get_location_summary(mock_location_name)
        assert_equal(response, mock_location_summary)

    def test_extract_location_summary(self):
        mock_location_summary = TestWikipediaRequest.mock_location_summary
        non_filtered_description = TestWikipediaRequest.non_filtered_description
        response = self.extract_location_summary(mock_location_summary)
        assert_equal(response, non_filtered_description)

    def test_filter_location_summary(self):
        non_filtered_description = TestWikipediaRequest.non_filtered_description
        filtered_description = TestWikipediaRequest.filtered_description
        response = self.filter_location_summary(non_filtered_description)
        assert_equal(response, filtered_description)

    @patch('app.controller.api_folder.api_wikipedia.requests.get')
    def test_get_coordinates(self, mock_get):
        mock_location_name = TestWikipediaRequest.mock_location_name
        mock_draft_coordinates = TestWikipediaRequest.mock_draft_coordinates
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_draft_coordinates
        response = self.get_coordinates(mock_location_name)
        assert_equal(response, mock_draft_coordinates)

    def test_filter_coordinates(self):
        mock_draft_coordinates = TestWikipediaRequest.mock_draft_coordinates
        filtered_coordinates = TestWikipediaRequest.filtered_coordinates
        response = self.filter_coordinates(mock_draft_coordinates)
        assert_equal(response, filtered_coordinates)

    def test_from_question_to_summary(self):
        question = TestWikipediaRequest.location_search
        check_important_words = TestWikipediaRequest.check_important_words
        summary = self.from_question_to_summary(question)
        assert all(map(lambda w: w in summary, check_important_words))

    def test_from_question_to_coordinates(self):
        question = TestWikipediaRequest.mock_location_name
        test_filtered_coordinates = TestWikipediaRequest.filtered_coordinates
        coordinates = self.from_question_to_coordinates(question)
        assert test_filtered_coordinates == coordinates

    def test_from_question_to_coordinates_not_ok(self):
        question = TestWikipediaRequest.article_without_coordinates
        coordinates = self.from_question_to_coordinates(question)
        assert coordinates == None

    def test_from_question_to_summary_not_ok(self):
        question = TestWikipediaRequest.non_existant_article
        summary = self.from_question_to_summary(question)
        assert summary == None

