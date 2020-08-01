import requests
from app.controller import config
from app.controller.api_folder.api_wikipedia import get_draft_location, sort_out_exact_location_name, get_location_summary, filter_location_summary
from pytest import mark
from tests.conftest import TestConfigureKeyWords
from nose.tools import assert_true, assert_is_not_none, assert_list_equal, assert_equal
from unittest.mock import Mock, patch


def configure_keywords(keywords):
    keywords = "%20".join(keywords.split())
    return keywords


def set_request(keywords):
    pass


def get_summary():
    pass


@mark.parametrize("test_input, expected", TestConfigureKeyWords.strings_to_test)
def test_configure_keywords(test_input, expected):
    assert configure_keywords(test_input) == expected


def test_connection_ok():
    response = requests.get(config.WIKI_ROOT)
    assert_true(response.ok)

@patch('app.controller.api_folder.api_wikipedia.requests.get')
def test_get_draft_location_when_response_is_ok(mock_get):
    mock_draft_location = {
        "batchcomplete": "",
        "continue": {
        "sroffset": 1,
        "continue": "-||"},
        "query": {
            "searchinfo": {
                "totalhits": 2091},
            "search": [
            {
                "ns": 0,
                "title": "Hôtel des Invalides",
                "pageid": 75747,
                "size": 73613,
                "wordcount": 8113,
                "snippet": "articles homonymes, voir <span class=\"searchmatch\">Invalides</span>. <span class=\"searchmatch\">Hôtel</span> des <span class=\"searchmatch\">Invalides</span> Vue aérienne. modifier - modifier le code - modifier Wikidata <span class=\"searchmatch\">L’hôtel</span> des <span class=\"searchmatch\">Invalides</span> est un monument parisien",
                "timestamp": "2020-07-13T20:49:09Z"}
            ]}
        }
    location_search = 'hotel invalides'
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_draft_location
    response = get_draft_location(location_search)
    assert_equal(response.json(), mock_draft_location)


def test_sort_out_exact_location_name():
    mock_location_name = "Hôtel des Invalides"
    mock_draft_location = {
        "batchcomplete": "",
        "continue": {
        "sroffset": 1,
        "continue": "-||"},
        "query": {
            "searchinfo": {
                "totalhits": 2091},
            "search": [
            {
                "ns": 0,
                "title": "Hôtel des Invalides",
                "pageid": 75747,
                "size": 73613,
                "wordcount": 8113,
                "snippet": "articles homonymes, voir <span class=\"searchmatch\">Invalides</span>. <span class=\"searchmatch\">Hôtel</span> des <span class=\"searchmatch\">Invalides</span> Vue aérienne. modifier - modifier le code - modifier Wikidata <span class=\"searchmatch\">L’hôtel</span> des <span class=\"searchmatch\">Invalides</span> est un monument parisien",
                "timestamp": "2020-07-13T20:49:09Z"}
            ]}
        }
    real_location_name = sort_out_exact_location_name(mock_draft_location)
    assert_equal(mock_location_name, real_location_name)


@patch('app.controller.api_folder.api_wikipedia.requests.get')
def test_get_location_summary(mock_get):
    mock_location_name = "Hôtel des Invalides"
    mock_location_summary = {
        "batchcomplete": "",
        "warnings": {
        "extracts": {
            "*": "HTML may be malformed and/or unbalanced and may omit inline images. Use at your own risk. Known problems are listed at https://www.mediawiki.org/wiki/Special:MyLanguage/Extension:TextExtracts#Caveats."
            }
        },
        "query": {"normalized": [{
            "from": "Hôtel_des_Invalides",
            "to": "Hôtel des Invalides"
            }],
        "pages": {
            "75747": {
                "pageid": 75747,
                "ns": 0,
                "title": "Hôtel des Invalides",
                "extract": "<p>L’<b>hôtel des Invalides</b> est un monument parisien dont la construction fut ordonnée par Louis <abbr class=\"abbr\" title=\"14\"><span>XIV</span></abbr> par l'édit royal du <time class=\"nowrap date-lien\" datetime=\"1670-02-24\" data-sort-value=\"1670-02-24\">24 février 1670</time>, pour abriter les invalides de ses armées. Aujourd'hui, il accueille toujours des invalides, mais également la cathédrale Saint-Louis des Invalides, plusieurs musées et une nécropole militaire avec notamment le tombeau de Napoléon <abbr class=\"abbr\" title=\"premier\">I<sup>er</sup></abbr>. C'est aussi le siège de hautes autorités militaires, comme le gouverneur militaire de Paris et rassemble beaucoup d'organismes dédiés à la mémoire des anciens combattants ou le soutien aux soldats blessés.\n</p><p>Cet immense complexe architectural, conçu par Libéral Bruand et Jules Hardouin-Mansart, est un des chefs-d’œuvre les plus importants de l'architecture classique française.\n</p><p>Ce site est desservi par les stations de métro Invalides, Varenne et La Tour-Maubourg. Avant 1860, il était situé dans le <abbr class=\"abbr\" title=\"Dixième\">10<sup>e</sup></abbr> arrondissement « ancien » d'où l'enregistrement du décès des militaires dans l'« état civil reconstitué » de la capitale qu'on peut trouver dans différentes bases de données.\n</p>\n\n\n"
                    }
                }
            }
        }
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_location_summary
    response = get_location_summary(mock_location_name)
    assert_equal(response.json(), mock_location_summary)


def test_filter_location_summary():
    non_filtered_description = "<p>L’<b>hôtel des Invalides</b> est un monument parisien dont la construction fut ordonnée par Louis <abbr class=\"abbr\" title=\"14\"><span>XIV</span></abbr> par l'édit royal du <time class=\"nowrap date-lien\" datetime=\"1670-02-24\" data-sort-value=\"1670-02-24\">24 février 1670</time>, pour abriter les invalides de ses armées. Aujourd'hui, il accueille toujours des invalides, mais également la cathédrale Saint-Louis des Invalides, plusieurs musées et une nécropole militaire avec notamment le tombeau de Napoléon <abbr class=\"abbr\" title=\"premier\">I<sup>er</sup></abbr>. C'est aussi le siège de hautes autorités militaires, comme le gouverneur militaire de Paris et rassemble beaucoup d'organismes dédiés à la mémoire des anciens combattants ou le soutien aux soldats blessés.\n</p><p>Cet immense complexe architectural, conçu par Libéral Bruand et Jules Hardouin-Mansart, est un des chefs-d’œuvre les plus importants de l'architecture classique française.\n</p><p>Ce site est desservi par les stations de métro Invalides, Varenne et La Tour-Maubourg. Avant 1860, il était situé dans le <abbr class=\"abbr\" title=\"Dixième\">10<sup>e</sup></abbr> arrondissement « ancien » d'où l'enregistrement du décès des militaires dans l'« état civil reconstitué » de la capitale qu'on peut trouver dans différentes bases de données.\n</p>\n\n\n"
    filtered_description = "L’ hôtel des Invalides est un monument parisien dont la construction fut ordonnée par Louis XIV par l'édit royal du 24 février 1670, pour abriter les invalides de ses armées. Aujourd'hui, il accueille toujours des invalides, mais également la cathédrale Saint-Louis des Invalides, plusieurs musées et une nécropole militaire avec notamment le tombeau de Napoléon I. C'est aussi le siège de hautes autorités militaires, comme le gouverneur militaire de Paris et rassemble beaucoup d'organismes dédiés à la mémoire des anciens combattants ou le soutien aux soldats blessés. Cet immense complexe architectural, conçu par Libéral Bruand et Jules Hardouin-Mansart, est un des chefs-d’œuvre les plus importants de l'architecture classique française. Ce site est desservi par les stations de métro Invalides, Varenne et La Tour-Maubourg. Avant 1860, il était situé dans le 10e arrondissement « ancien » d'où l'enregistrement du décès des militaires dans l'« état civil reconstitué » de la capitale qu'on peut trouver dans différentes bases de données."
    response = filter_location_summary(non_filtered_description)
    assert_equal (response, non_filtered_description)

def test_get_coordinates():
    mock_coordinates = {
        "batchcomplete":"",
        "query":{"pages":
        {"75747":{"pageid":75747,"ns":0,"title":"H\u00f4tel des Invalides",
        "coordinates":[{"lat":48.86,"lon":2.311944,"primary":"","globe":"earth"}]}}}}
    pass