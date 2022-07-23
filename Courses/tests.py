from unittest.mock import patch

from django.test import TestCase, Client
from .services.services import CoursesService
from .models import Courses
# Create your tests here.

client = Client()
class CoursesTest(TestCase):
    def test_high_price(self):
        is_high_price = CoursesService.is_high_price(1000)
        self.assertEqual(is_high_price, True)

    def test_not_high_price(self):
        is_high_price = CoursesService.is_high_price(100)
        self.assertEqual(is_high_price, False)

    def setUp(self):
        Courses.objects.create(title='b4', price=2000, content='nd4')
        Courses.objects.create(title='bai 8', price=200, content='noi dung 8')

    def test_high_price1(self):
        response = client.get('/Courses/high_price/')
        result = {
            'data': [
                {
                    'title': 'b4',
                    'price': 2000,
                    'content': 'nd4',
                }
            ]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result)

    @patch('Courses.services.services.CoursesService.is_high_price', return_value=False)
    def test_high_price2(self, is_high_price):
        response = client.get('/Courses/high_price/')
        result = {
            'data': [
            ]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result)




