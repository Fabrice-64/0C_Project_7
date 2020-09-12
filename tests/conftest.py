from config import GooglePath, Config


class TestParameters():
    question1 = [
        """Bonjour ChatBot, pourrais-tu me parler des Champs-Elysées?
        Bisous à tout le monde""",
        'parler Champs Elysées ? monde',
        [('parler', 'VERB'), ('Champs', 'PROPN'), ('Elysées', 'PROPN'),
            ('?', 'PUNCT'), ('monde', 'NOUN')],
        ('Champs Elysées')
    ]

    question2 = [
        """Coucou mon Papounet, toi qui sais tout,
        c\'est quoi, la Vallée des Saints ?""",
        'sais Vallée Saints ?',
        [('sais', 'VERB'), ('Vallée', 'NOUN'), ('Saints', 'PROPN'),
            ('?', 'PUNCT')],
        ('Vallée Saints')
        ]

    question3 = [
        'Salut Fab, tu connais le Musée des Invalides?',
        'connais Musée Invalides ?',
        [('connais', 'VERB'), ('Musée', 'NOUN'), ('Invalides', 'PROPN'),
            ('?', 'PUNCT')],
        ('Musée Invalides')
        ]

    question4 = [
        """Bonjour, PapyBot. J\'espère que vous allez tous bien à la maison.
        Alors, j\'ai une question pour toi.\
        Que connais-tu du chateau de Versailles?""",
        """. espère allez maison . Alors question . Que connais chateau Versailles ?""",
        [('.', 'PUNCT'), ('espère', 'VERB'), ('allez', 'VERB'),
            ('maison', 'NOUN'), ('.', 'PUNCT'), ('Alors', 'ADV'),
            ('question', 'NOUN'), ('.', 'PUNCT'), ('Que', 'PRON'),
            ('connais', 'VERB'), ('chateau', 'NOUN'), ('Versailles', 'PROPN'),
            ('?', 'PUNCT')],
        ('chateau Versailles')
        ]

    question5 = ["Salut tu vas bien han ?",
                    "han ?",
                [('han', 'PROPN'), ("?", "PUNCT")],
                ('han')]

    questions_tokenize = [
        (question1[0], question1[1]),
        (question2[0], question2[1]),
        (question3[0], question3[1]),
        (question4[0], question4[1]),
        (question5[0], question5[1])
        ]

    tag_tokens = [
        (question1[1], question1[2]),
        (question2[1], question2[2]),
        (question3[1], question3[2]),
        (question4[1], question4[2]),
        (question5[1], question5[2])
        ]

    filtered_words = [
        (question1[2], question1[3]),
        (question2[2], question2[3]),
        (question3[2], question3[3]),
        (question4[2], question4[3]),
        (question5[2], question5[3])
        ]

    parsing_process = [
        (question1[0], question1[3]),
        (question2[0], question2[3]),
        (question3[0], question3[3]),
        (question4[0], question4[3]),
        (question5[0], question5[3])

        ]


class TestConfigureKeyWords():
    strings_to_test = [
        (TestParameters.question1[3], 'Champs Elysées Paris'),
        (TestParameters.question2[3], 'Vallée Saints'),
        (TestParameters.question3[3], 'Musée Invalides'),
        (TestParameters.question4[3], 'chateau Versailles')
    ]


class TestWikipediaRequest():
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
    
    non_filtered_description = "<p>L’<b>hôtel des Invalides</b> est un monument parisien dont la construction fut ordonnée par Louis <abbr class=\"abbr\" title=\"14\"><span>XIV</span></abbr> par l'édit royal du <time class=\"nowrap date-lien\" datetime=\"1670-02-24\" data-sort-value=\"1670-02-24\">24 février 1670</time>, pour abriter les invalides de ses armées. Aujourd'hui, il accueille toujours des invalides, mais également la cathédrale Saint-Louis des Invalides, plusieurs musées et une nécropole militaire avec notamment le tombeau de Napoléon <abbr class=\"abbr\" title=\"premier\">I<sup>er</sup></abbr>. C'est aussi le siège de hautes autorités militaires, comme le gouverneur militaire de Paris et rassemble beaucoup d'organismes dédiés à la mémoire des anciens combattants ou le soutien aux soldats blessés.\n</p><p>Cet immense complexe architectural, conçu par Libéral Bruand et Jules Hardouin-Mansart, est un des chefs-d’œuvre les plus importants de l'architecture classique française.\n</p><p>Ce site est desservi par les stations de métro Invalides, Varenne et La Tour-Maubourg. Avant 1860, il était situé dans le <abbr class=\"abbr\" title=\"Dixième\">10<sup>e</sup></abbr> arrondissement « ancien » d'où l'enregistrement du décès des militaires dans l'« état civil reconstitué » de la capitale qu'on peut trouver dans différentes bases de données.\n</p>\n\n\n"

    filtered_description = "L’hôtel des Invalides est un monument parisien dont la construction fut ordonnée par Louis XIV par l'édit royal du 24 février 1670, pour abriter les invalides de ses armées. Aujourd'hui, il accueille toujours des invalides, mais également la cathédrale Saint-Louis des Invalides, plusieurs musées et une nécropole militaire avec notamment le tombeau de Napoléon Ier. C'est aussi le siège de hautes autorités militaires, comme le gouverneur militaire de Paris et rassemble beaucoup d'organismes dédiés à la mémoire des anciens combattants ou le soutien aux soldats blessés.\nCet immense complexe architectural, conçu par Libéral Bruand et Jules Hardouin-Mansart, est un des chefs-d’œuvre les plus importants de l'architecture classique française.\nCe site est desservi par les stations de métro Invalides, Varenne et La Tour-Maubourg. Avant 1860, il était situé dans le 10e arrondissement « ancien » d'où l'enregistrement du décès des militaires dans l'« état civil reconstitué » de la capitale qu'on peut trouver dans différentes bases de données.\n\n\n\n"

    mock_draft_coordinates = {
            "batchcomplete":"",
            "query":{"pages":
            {"75747":{"pageid":75747,"ns":0,"title":"H\u00f4tel des Invalides",
            "coordinates":[{"lat":48.86,"lon":2.311944,"primary":"","globe":"earth"}
            ]}}}}

    filtered_coordinates = {"lat":48.86,"lon":2.311944,"primary":"","globe":"earth"}

    check_important_words = ('Invalides', '1860','classique', 'militaires', 'arrondissement', 'bases de données')

    article_without_coordinates = "Napoléon Ier"

    non_existant_article = "None"

class TestGoogleApiParams(GooglePath):
    location = "hôtel des Invalides"
    google_response = GooglePath.GOOGLE_ROOT_DYNAMIC + 'key=' + Config.GOOGLE_API_KEY + '&q=h%C3%B4tel+des+Invalides&language=fr&zoom=11&region=fr'
    test_google_params = [(location, google_response)]


