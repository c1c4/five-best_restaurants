import unittest

from app import app


class RestaurantsTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_empty_restaurant_list(self):
        response = self.app.get('/restaurants?cuisine=chia')

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(response.json))

    def test_restaurant_error_406(self):
        response = self.app.get('/restaurants?price=chia')

        self.assertEqual(406, response.status_code)

    def test_best_matched_5_items(self):
        response = self.app.get('/restaurants?cuisine=kor')

        self.assertEqual(200, response.status_code)
        self.assertEqual(5, len(response.json))
