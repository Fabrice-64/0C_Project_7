

class TestParameters():
    question1 = [
        'Bonjour ChatBot, pourrais-tu me parler des Champs-Elysées, à Paris ? Bisous à tout le monde',
        'parler Champs Elysées Paris ? monde',
        [('parler', 'VERB'), ('Champs', 'PROPN'), ('Elysées', 'PROPN'),
            ('Paris', 'PROPN'), ('?', 'PUNCT'), ('monde', 'NOUN')],
        ('Champs Elysées Paris')
    ]

    question2 = [
        'Coucou mon Papounet, toi qui sais tout, c\'est quoi, la Vallée des Saints ?',
        'sais Vallée Saints ?',
        [('sais', 'VERB'), ('Vallée', 'NOUN'), ('Saints', 'PROPN'), ('?', 'PUNCT')],
        ('Vallée Saints')
        ]

    question3 = [
        'Salut Fab, tu connais le Musée des Invalides?',
        'connais Musée Invalides ?',
        [('connais', 'VERB'), ('Musée', 'NOUN'), ('Invalides', 'PROPN'), ('?', 'PUNCT')],
        ('Musée Invalides')
        ]

    questions_tokenize = [
        (question1[0], question1[1]),
        (question2[0], question2[1]),
        (question3[0], question3[1])
        ]

    tag_tokens = [
        (question1[1], question1[2]),
        (question2[1], question2[2]),
        (question3[1], question3[2])
        ]

    filtered_words = [
        (question1[2], question1[3]),
        (question2[2], question2[3]),
        (question3[2], question3[3]),
        ]

    parsing_process = [
        (question1[0], question1[3]),
        (question2[0], question2[3]),
        (question3[0], question3[3])
        ]


class TestConfigureKeyWords():
    strings_to_test = [
        (TestParameters.question1[3], 'Champs%20Elysées%20Paris'),
        (TestParameters.question2[3], 'Vallée%20Saints'),
        (TestParameters.question3[3], 'Musée%20Invalides')
    ]

