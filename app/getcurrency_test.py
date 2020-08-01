import sys
sys.path.append(".")
import unittest
from configparser import ConfigParser
import requests
import responses
from unittest.mock import patch, mock_open
from app.getcurrency import CurrencyDownloader

# read url from config file
config = ConfigParser()
config.read('../config/config.ini')
url = config.get('URLS', 'URL')

# write a class to test the methods written in getcurrency.py file.
# unittest.TestCase allow us with testing capabilities
class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.currencyDownloader = CurrencyDownloader(url)
    # method name should always start with test 
    @responses.activate
    def test_checkURL(self):
        responses.add(**{
            'method': responses.GET,
            'url': self.currencyDownloader.url,
            'body': '{"error": "reason"}',
            'status': 404,
            'content_type': 'application/json'
        })

        response = requests.get(url)

        self.assertEqual({'error': 'reason'}, response.json())
        self.assertEqual(404, response.status_code)

# run the code within the conditional
if __name__ == '__main__':
    unittest.main()