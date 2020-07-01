import unittest
import requests


class Test(unittest.TestCase):
    def test_check_server(self):
        response = requests.get('http://localhost:5000')
        assert response.status_code == 200

    def test_enter_search(self):
        self.question1 = "Bonjour, parle-moi de la Cité Paradis, à Paris"
        self.assertEqual(self.question1.enter_search,
                         "Bonjour, parle-moi de la Cité Paradis, à Paris")

    def test_search_parsing(self):
        self.question1 = "Bonjour, parle-moi de la Cité Paradis, à Paris?"
        self.question2 = "Bonjour, qu'il y a-t-il Rue de Rivoli, à Paris?"
        self.assertEqual(self.question1.search_parsing,
                         {'street': 'Cité Paradis', 'city': 'Paris'})
        self.assertEqual(self.question1.search_parsing,
                         {'street': 'Rue de Rivoli', 'city': 'Paris'})


if __name__ == '__main__':
    unittest.main(verbosity=2)
