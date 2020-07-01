import unittest
import requests


class Test(unittest.TestCase):
    def test_check_server(self):
        response = requests.get('http://localhost:5000')
        assert response.status_code == 200




if __name__ == '__main__':
    unittest.main(verbosity=2)
