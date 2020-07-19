
ROOT = '/Users/fabricejaouen/DepotLocalGIT/OC_Project_7'
JAR = '/chatbot/resources/stanford-tagger-4.0.0/stanford-postagger.jar'
MODEL = '/chatbot/resources/stanford-tagger-4.0.0/models/french-ud.tagger'


class Path():
    PATH_TO_JAR = ROOT + JAR
    PATH_TO_MODEL = ROOT+MODEL


class TestParameters():
    questions = [
        ('Bonjour ChatBot, pourrais-tu me parler des Champs-Elysées,\
        à Paris ? Bisous à tout le monde', 'Champs-Elysées Paris'),
        ('Coucou mon Papounet, toi qui sais tout, c\'est quoi,\
        la Vallée des Saints ?', 'Vallée Saints'),
        ('Salut Fab, tu connais le musée des Invalides?', 'Musée Invalides')
    ]
