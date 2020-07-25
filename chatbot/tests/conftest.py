

class TestParameters():
    questions_tokenize = [
        ('Bonjour ChatBot, pourrais-tu me parler des Champs-Elysées, à Paris ? Bisous à tout le monde', 
        'parler Champs Elysées Paris ? monde'),
        ('Coucou mon Papounet, toi qui sais tout, c\'est quoi, la Vallée des Saints ?',
        'sais Vallée Saints ?'),
        ('Salut Fab, tu connais le Musée des Invalides?',
        'connais Musée Invalides ?')
    ]

    tag_tokens = [
        ('parler Champs Elysées Paris ? monde', [
            ('parler', 'VERB'), ('Champs', 'PROPN'), ('Elysées', 'PROPN'),
            ('Paris', 'PROPN'), ('?', 'PUNCT'), ('monde', 'NOUN')]),
        ('sais Vallée Saints ?', [
            ('sais', 'VERB'), ('Vallée', 'NOUN'), ('Saints', 'PROPN'),
            ('?', 'PUNCT')]),
        ('connais Musée Invalides ?', [
            ('connais', 'VERB'), ('Musée', 'NOUN'), ('Invalides', 'PROPN'),
            ('?', 'PUNCT')])
    ]

    filtered_words = [
        ([('parler', 'VERB'), ('Champs', 'PROPN'), ('Elysées', 'PROPN'),
            ('Paris', 'PROPN'), ('?', 'PUNCT'), ('monde', 'NOUN')],
            ('Champs Elysées Paris')),
        ([('sais', 'VERB'), ('Vallée', 'NOUN'), ('Saints', 'PROPN'),
            ('?', 'PUNCT')],
            ('Vallée Saints')),
        ([('connais', 'VERB'), ('Musée', 'NOUN'), ('Invalides', 'PROPN'),
            ('?', 'PUNCT')],
            ('Musée Invalides'))
    ]