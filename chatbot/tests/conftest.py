

class TestParameters():
    question1 = [
        'Bonjour ChatBot, pourrais-tu me parler des Champs-Elysées? Bisous à tout le monde',
        'parler Champs Elysées ? monde',
        [('parler', 'VERB'), ('Champs', 'PROPN'), ('Elysées', 'PROPN'),
            ('?', 'PUNCT'), ('monde', 'NOUN')],
        ('Champs Elysées')
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

    question4 = [
        'Bonjour, PapyBot. J\'espère que vous allez tous bien à la maison. Alors, j\'ai une question pour toi.  Que connais-tu du chateau de Versailles?',
         '. espère allez maison . Alors question . Que connais chateau Versailles ?',
        [('.', 'PUNCT'), ('espère', 'VERB'), ('allez', 'VERB'), ('maison', 'NOUN'), ('.', 'PUNCT'),
        ('Alors', 'ADV'), ('question', 'NOUN'), ('.', 'PUNCT'), ('Que', 'PRON'),
        ('connais', 'VERB'), ('chateau', 'NOUN'), ('Versailles', 'PROPN'), ('?', 'PUNCT')
        ],
        ('chateau Versailles')
        ]

    questions_tokenize = [
        (question1[0], question1[1]),
        (question2[0], question2[1]),
        (question3[0], question3[1]),
        (question4[0], question4[1])
        ]

    tag_tokens = [
        (question1[1], question1[2]),
        (question2[1], question2[2]),
        (question3[1], question3[2]),
        (question4[1], question4[2])
        ]

    filtered_words = [
        (question1[2], question1[3]),
        (question2[2], question2[3]),
        (question3[2], question3[3]),
        (question4[2], question4[3])
        ]

    parsing_process = [
        (question1[0], question1[3]),
        (question2[0], question2[3]),
        (question3[0], question3[3]),
        (question4[0], question4[3])
        ]


class TestConfigureKeyWords():
    strings_to_test = [
        (TestParameters.question1[3], 'Champs Elysées Paris'),
        (TestParameters.question2[3], 'Vallée Saints'),
        (TestParameters.question3[3], 'Musée Invalides'),
        (TestParameters.question4[3], 'chateau Versailles')
    ]

